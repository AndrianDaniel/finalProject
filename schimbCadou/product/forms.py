from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'price', 'description', 'category', 'product_picture']

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the product name'}),
			'price': forms.NumberInput(
				attrs={'class': 'form-control', 'placeholder': 'Please enter the product price'}),
			'description': forms.Textarea(
				attrs={'class': 'form-control', 'placeholder': 'Please enter the product description'}),
			'category': forms.Select(attrs={'class': 'form-select'}),
		}


class ProductUpdateForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'price', 'description', 'category', 'product_picture']

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the product name'}),
			'price': forms.NumberInput(
				attrs={'class': 'form-control', 'placeholder': 'Please enter the product price'}),
			'description': forms.Textarea(
				attrs={'class': 'form-control', 'placeholder': 'Please enter the product description'}),
			'category': forms.Select(attrs={'class': 'form-select'}),
		}

class ExchangeAcceptanceForm(forms.Form):
	choices = [('a', 'Accepted'), ('d', 'Declined')]

	request_id = forms.IntegerField()
	action = forms.ChoiceField(choices=choices)

class ProductReportForm(forms.Form):
	product = forms.IntegerField()
	comment = forms.CharField(widget=forms.Textarea())

	class Meta:
		fields = ['product', 'comment']








