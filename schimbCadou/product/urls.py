from django.urls import path

from . import views

urlpatterns = [
	path('create_product/', views.ProductCreateView.as_view(), name='create-product'),
	path('list_products/', views.ProductListView.as_view(), name='list-products'),
	path('update_product/<int:pk>', views.ProductUpdateView.as_view(), name='update-product'),
	path('delete_product/<int:pk>', views.ProductDeleteView.as_view(), name='delete-product'),
	path('get_history/', views.HistoryProductListView.as_view(), name='get-history'),
	path('details_product/<int:pk>', views.ProductDetailView.as_view(), name='details-product'),
	path('search_results/', views.search_product, name='search-results'),
	path('category_view/<pk>', views.CategoryDetailView.as_view(), name='category-view'),
	path('handle_exchange/', views.handle_create_exchange, name='handle-exchange'),
	path('accept_exchange/', views.handle_exchange, name='accept-exchange'),
	path('list_requests', views.ReceivedExchangeRequestList.as_view(), name='list-requests'),
	path('sent_requests', views.SentExchangeRequestList.as_view(), name='sent-requests'),
	path('handle_buy',views.handle_buy, name='handle-buy'),
]
