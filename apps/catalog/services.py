from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings

from apps.catalog.models import Category


def send_email(title: str) -> None:
    """Sends an email with congratulations"""
    send_mail(
        'New achievement!',
        f'Congratulations! You article {title} has got 100 views!',
        settings.EMAIL_HOST_USER,
        ['test3112django@yandex.ru']
    )
def get_categories_cache():
    if settings.CACHE_ENABLED:
        key = 'categories_list'
        categories_list = cache.get(key)
        if categories_list is None:
            categories_list = Category.objects.all()
            cache.set(key, categories_list)
    else:
        categories_list = Category.objects.all()
    return categories_list


