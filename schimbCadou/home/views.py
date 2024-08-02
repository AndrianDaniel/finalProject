from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from product.models import Category, Product


class HomeTemplateView(TemplateView):
	template_name = 'home/homepage.html'

	def get_context_data(self, **kwargs):
		context = super(HomeTemplateView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['products'] = Product.objects.filter(product_picture__isnull=False).exclude(product_picture="")

		return context


