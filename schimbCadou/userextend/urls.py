from . import views
from django.urls import path

urlpatterns = [
	path('create_user/', views.UserCreateView.as_view(), name='create-user')
]
