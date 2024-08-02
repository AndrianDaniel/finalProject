from django.contrib import admin
from .models import Category, Product, ExchangeRequestModel, WalletModel

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(WalletModel)


class ExchangeRequestModelAdmin(admin.ModelAdmin):
	fields = ['owner', 'requester', 'base_product', 'exchange_for', 'accepted', 'created_at', 'updated_at']
	readonly_fields = ['created_at', 'updated_at']
	class Meta:
		model = ExchangeRequestModel

admin.site.register(ExchangeRequestModel, ExchangeRequestModelAdmin)
