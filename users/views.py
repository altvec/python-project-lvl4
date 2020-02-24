# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from users.forms import UserCreationForm


def register_user(request):
    """User register function."""
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info = (  # noqa: WPS110
                request,
                "Thanks for registering. You're now logged in.",
            )
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, user)
            return redirect('/')
    return render(request, 'registration/register.html', {'form': form})
