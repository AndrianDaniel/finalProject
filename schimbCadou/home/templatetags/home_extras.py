from django import template

register = template.Library()


@register.filter
def count_excluding_own_products(products, user):
	return products.exclude(user=user).count()
