from django.core.mail import send_mail
from django.conf import settings

def send_email(title):
    send_mail(
        'New achievement!',
        f'Congratulations! You article {title} has got 100 views!',
        settings.EMAIL_HOST_USER,
        ['blokhnina.tatiana@yandex.ru']
    )
