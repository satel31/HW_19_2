from django.urls import path
from apps.catalog.views import homepage, contacts

app_name = 'catalog'

urlpatterns = [
    path('', homepage),
    path('contacts/', contacts)
]
