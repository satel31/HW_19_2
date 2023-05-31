from django.urls import path
from apps.catalog.views import homepage, contacts, products, add_products

app_name = 'catalog'

urlpatterns = [
    path('home/', homepage),
    path('contacts/', contacts),
    path('', products, name='products'),
    path('add_products/', add_products, name='add_products')
]

