# -*- coding: utf-8 -*-

from django.views.generic import ListView

from tasks.models import Task


class TaskListView(ListView):
    """A view for list of tasks."""

    model = Task
    template_name = 'tasks/main.html'
    context_object_name = 'tasks'
    ordering = ['-pk']
