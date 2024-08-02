import datetime
import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .forms import ProductForm, ProductUpdateForm,ExchangeAcceptanceForm
from .models import Product, HistoryProduct, Category, ExchangeRequestModel
from schimbCadou import settings


class ProductCreateView(LoginRequiredMixin, CreateView):
	template_name = 'product/create_product.html'
	model = Product
	form_class = ProductForm
	success_url = reverse_lazy('home-page')

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		context['now'] = datetime.datetime.now()
		context['products'] = Product.objects.all()

		return context

	def form_valid(self, form):
		if form.is_valid():
			new_product = form.save(commit=False)
			new_product.user = self.request.user
			new_product.name = new_product.name.title()
			new_product.save()

			json_user_details = {
				'name': new_product.name
			}

			HistoryProduct.objects.create(message=json_user_details, created_at=datetime.datetime.now(),
										  user=self.request.user)

		return redirect('list-products')


class ProductListView(LoginRequiredMixin, ListView):
	template_name = 'product/list_of_products.html'
	model = Product
	context_object_name = 'all_products'

	def get_queryset(self):
		return Product.objects.filter(user=self.request.user)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'product/update_product.html'
	model = Product
	form_class = ProductUpdateForm
	success_url = reverse_lazy('list-products')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'product/delete_product.html'
	model = Product
	success_url = reverse_lazy('list-products')


class HistoryProductListView(LoginRequiredMixin, ListView):
	template_name = 'product/history_product.html'
	model = HistoryProduct
	context_object_name = 'products_history'

	def get_queryset(self):
		return HistoryProduct.objects.filter(user=self.request.user)


class ProductDetailView(LoginRequiredMixin, DetailView):
	template_name = 'product/details_product.html'
	model = Product


class CategoryDetailView(DetailView):
	template_name = 'product/category_view.html'
	model = Category

	def get_context_data(self, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(**kwargs)
		context['products'] = Product.objects.filter(category=self.get_object()).exclude(user=self.request.user)
		context['categories'] = Category.objects.all()
		context['personal_products'] = Product.objects.filter(user=self.request.user)
		return context


@require_POST
def search_product(request):
	data = request.POST
	search_term = data.get('search_term')
	if search_term is None or search_term == '':
		return HttpResponse(status=400)
	else:
		all_products = Product.objects.all()
		search_results = all_products.filter(name__contains=search_term).exclude(user=request.user)
		personal_products = Product.objects.filter(user=request.user)
		return render(request, 'product/search_results.html',
					  context={'products': search_results,
							   'search_criteria': search_term,
							   'personal_products': personal_products,
							   'categories': Category.objects.all()
							   })


@require_POST
def handle_create_exchange(request):
	selected_product_ids = request.POST.getlist('product_ids')

	exchange_product_id = request.POST.get('product_id')

	# Transformă lista de ID-uri în obiecte Product
	selected_products = Product.objects.filter(id__in=selected_product_ids)

	# Ne asiguram ca produsul are o valoare
	exchange_product = get_object_or_404(Product, pk=exchange_product_id)

	if not selected_products:
		return HttpResponse(status=404, content='No products found')
	else:
		exchange_request = ExchangeRequestModel.objects.create(owner=exchange_product.user,
															   requester=request.user,
															   base_product=exchange_product, )
		for product in selected_products:
			exchange_request.exchange_for.add(product)

		exchange_request.save()

	return HttpResponseRedirect('/sent_requests')

@require_POST
def handle_exchange(request):
	form = ExchangeAcceptanceForm(data=request.POST)

	if form.is_valid():
		cleaned_data = form.cleaned_data
		exchange_request_id = cleaned_data.get('request_id')
		exchange_request = get_object_or_404(ExchangeRequestModel, pk=exchange_request_id)
		if exchange_request.owner == request.user:
			action = cleaned_data.get("action")
			if action == 'a':
				exchange_request.handle_exchange()
				return HttpResponse(status=202,content="Exchange handled successfully!")
			elif action=='d':
				exchange_request.decline_offer()
				return HttpResponse(status=202, content="Exchange declined successfully!")
			else:
				return HttpResponse(status=400,content="Actiune invalida")

		else:
			return HttpResponse(status=401,content="Aceasta cerere nu iti apartine")
	else:
		return HttpResponse(status=400, content="Formular completat gresit")

@require_POST
def handle_buy(request):
	buy_product_id = request.POST.get('product_id')
	buy_product = get_object_or_404(Product, pk=buy_product_id)

	product_price = buy_product.price
	buyer_wallet = request.user.wallet
	seller_wallet = buy_product.user.wallet

	if buyer_wallet.amount >= product_price:
		buyer_wallet.amount -= product_price
		seller_wallet.amount += product_price

		buyer_wallet.save()
		seller_wallet.save()

		buy_product.user_id = request.user.id
		buy_product.save()

		buy_product.clean_up_offers()

	else:
		return HttpResponse(status=403, content="Fonduri insuficiente")



	return HttpResponseRedirect('/list_products')

class ReceivedExchangeRequestList(LoginRequiredMixin,ListView):
	template_name = 'product/received_exchange_requests.html'
	model = ExchangeRequestModel
	context_object_name = 'exchange_requests'

	def get_queryset(self):
		query_set = self.model.objects.filter(owner=self.request.user,accepted='u').prefetch_related("exchange_for")
		return query_set

class SentExchangeRequestList(LoginRequiredMixin, ListView):
	template_name = 'product/sent_exchange_requests.html'
	model = ExchangeRequestModel
	context_object_name = 'exchange_requests'

	def get_queryset(self):
		query_set = self.model.objects.filter(requester=self.request.user).prefetch_related("exchange_for")
		return query_set

