from django.urls import path
from apps.catalog.views import homepage, contacts, products

app_name = 'catalog'

urlpatterns = [
    path('', homepage),
    path('contacts/', contacts),
    path('products/', products),
]

