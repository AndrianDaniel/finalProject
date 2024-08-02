import os

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserForm
from product.models import WalletModel


class UserCreateView(CreateView):
	template_name = 'userextend/create_user.html'
	model = User
	form_class = UserForm
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.first_name = new_user.first_name.title()
			new_user.last_name = new_user.last_name.title()

			subject = 'Adaugare cont nou'
			details = {
				'fullname': f'{new_user.first_name} {new_user.last_name}',
				'user_name': new_user.username
			}

			message_file = open('./templates/mail.html')
			message_html = message_file.read()
			message_html.replace('{{ fullname }}', details['fullname'])
			message_html.replace('{{ user_name }}', details['user_name'])


			message_text = "text1234"
			send_mail(subject, message_text,
					  'no_replay@giftexchange.ro',
					  [new_user.email],
					  html_message=message_html)

			new_user.save()

			WalletModel.objects.create(user=new_user)

			return redirect('login')
