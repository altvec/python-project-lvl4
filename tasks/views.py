# -*- coding: utf-8 -*-

from django.shortcuts import render

from tasks.models import Task


def home(request):
    """Simple home view with list of all tasks."""
    context = {
        'tasks': Task.objects.all(),
    }
    return render(request, 'tasks/main.html', context)
