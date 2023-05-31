from django.urls import path
from apps.catalog.views import homepage, contacts, products

app_name = 'catalog'

urlpatterns = [
    path('home/', homepage),
    path('contacts/', contacts),
    path('', products),
]

