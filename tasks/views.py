# -*- coding: utf-8 -*-

from django.shortcuts import render


def home(request):  # noqa: D103
    return render(request, 'home.html')
