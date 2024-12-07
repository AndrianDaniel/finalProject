from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name.title()


class Product(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
	description = models.TextField(max_length=400)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	product_picture = models.ImageField(upload_to='product_pictures/', null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def delete(self, *args, **kwargs):
		self.product_picture.delete()
		json_data_delete = {'name': self.name, 'action': 'delete'}
		HistoryProduct.objects.create(message=json_data_delete,user=self.user)
		super(Product, self).delete(*args, **kwargs)

	def clean_up_offers(self,exclude=None):

		# Toate celelalte oferte unde produsul curent este in baza base_product
		offers_to_decline = self.exchange_offers.all()

		if exclude:
			offers_to_decline = offers_to_decline.exclude(id=exclude)

		# Toate celelalte oferte unde produsul curent este in lista de exchange_for
		offers_to_delete = self.exchange_offers_for.all()

		if exclude:
			offers_to_delete = offers_to_delete.exclude(id=exclude)

		for offer in offers_to_decline:
			offer.decline_offer()

		for offer in offers_to_delete:
			offer.delete()

	def __str__(self):
		return f'{self.name}'


class HistoryProduct(models.Model):
	message = models.JSONField()
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return (self.message.get('name') or self.id)

class  ExchangeRequestModel(models.Model):
	choices = [('a', 'Accepted'), ('d', 'Declined'), ('u', 'Unprocessed')]

	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='original_owner')
	requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requester')
	base_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='exchange_offers')
	exchange_for = models.ManyToManyField(Product, related_name='exchange_offers_for')
	accepted = models.CharField(max_length=1, choices=choices, default='u')

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def handle_exchange(self):

		offer: ExchangeRequestModel  # type hinting

		selected_products = self.exchange_for.all()

		exchange_product = self.base_product

		# Schimba produsele intre useri
		for product in selected_products:
			product.user = self.owner
			product.save()

			product.clean_up_offers(self.id)

		exchange_product.user = self.requester
		exchange_product.save()

		self.accepted = "a"
		self.save()

		self.base_product.clean_up_offers(self.id)

	def decline_offer(self):
		self.accepted = 'd'
		self.save()

class WalletModel (models.Model):
	user = models.OneToOneField(User, related_name='wallet', on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)

class ProductReportModel (models.Model):
	choices = [('r', 'Resolved'), ('d', 'Declined'), ('u', 'Unprocessed')]

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	comment = models.TextField(max_length=450)

	resolution = models.CharField(max_length=1,choices=choices, default='u')
