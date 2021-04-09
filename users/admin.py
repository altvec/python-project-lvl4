# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import UserChangeForm, UserCreationForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    """User representation class."""

    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
