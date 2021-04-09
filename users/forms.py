# -*- coding: utf-8 -*-

from django.contrib.auth import forms
from users.models import CustomUser


class UserCreationForm(forms.UserCreationForm):
    """User creation form."""

    class Meta(forms.UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')


class UserChangeForm(forms.UserChangeForm):
    """User change form."""

    class Meta(forms.UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email')
