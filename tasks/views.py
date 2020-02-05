# -*- coding: utf-8 -*-

from django.shortcuts import render
from tasks.models import Task


def home(request):
    context = {
        'tasks': Task.objects.all(),
    }
    return render(request, 'tasks/main.html', context)
