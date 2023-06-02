from django.urls import path
from apps.catalog.views import ProductListView, ProductCreateView, ProductByPageListView
#products,add_products, all_products

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('add_products/', ProductCreateView.as_view(), name='add_products'),
    path('all_products/', ProductByPageListView.as_view(), name='all_products'),
]
