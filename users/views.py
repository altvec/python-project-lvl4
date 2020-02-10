# -*- coding: utf-8 -*-

from django.shortcuts import redirect, render

from users.forms import UserCreationForm


def register_user(request):
    """User register function."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
