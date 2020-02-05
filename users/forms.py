from django.contrib.auth import forms
from users.models import CustomUser


class UserCreationForm(forms.UserCreationForm):
    """User creation form."""

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class UserChangeForm(forms.UserChangeForm):
    """User change form."""

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
