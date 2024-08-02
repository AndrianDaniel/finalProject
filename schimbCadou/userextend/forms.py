from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Please enter a first name'})
		self.fields['last_name'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Please enter a last name'})
		self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter a email'})
		self.fields['password1'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Please enter a password'})
		self.fields['password2'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Please enter a password confirmation'})

class AuthenticationNewForm(AuthenticationForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Please enter your username'})
		self.fields['password'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Place enter your password'})
