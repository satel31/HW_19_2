from django.contrib.auth.forms import UserCreationForm

from apps.users.models import User


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password_1', 'password_2',)
