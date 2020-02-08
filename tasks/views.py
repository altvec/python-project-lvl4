# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from tasks.models import Task


class TaskListView(ListView):
    """A view for list of tasks."""

    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'
    ordering = ['-pk']


class TaskDetailView(DetailView):
    """Task details view."""

    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Task create view."""

    model = Task
    fields = ['name', 'description', 'tags', 'assigned_to', 'status']
    template_name = 'task_create.html'

    def form_valid(self, form):
        """Validate form."""
        form.instance.creator = self.request.user
        return super().form_valid(form)
