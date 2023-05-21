from django.urls import path
from catalog.views import CHANGE_NAME

app_name = CHANGE_NAME

urlpatterns = [
    path('', CHANGE_NAME, namespace='CHANGE_NAME'),
]