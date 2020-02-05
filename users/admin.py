from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
