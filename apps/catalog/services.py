from django.core.mail import send_mail
from django.conf import settings

def send_email(title: str) -> None:
    """Sends an email with congratulations"""
    send_mail(
        'New achievement!',
        f'Congratulations! You article {title} has got 100 views!',
        settings.EMAIL_HOST_USER,
        ['blokhnina.tatiana@yandex.ru']
    )

def transliterate(s: str) -> str:
    """Transliterate a string in russian for slug"""
    symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
               u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")

    tr = {ord(a): ord(b) for a, b in zip(*symbols)}
    slug = s.translate(tr)
    return slug
