# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

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


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Task delete view."""

    model = Task
    success_url = reverse_lazy('tasks-home')
    template_name = 'task_confirm_delete.html'

    def test_func(self):
        """Test task ownership before deleting."""
        task = self.get_object()
        return self.request.user == task.creator


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Task update view."""

    model = Task
    fields = ['name', 'description', 'tags', 'assigned_to', 'status']
    template_name = 'task_create.html'

    def form_valid(self, form):
        """Validate form."""
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Test task ownership berfore updating."""
        task = self.get_object()
        return self.request.user == task.creator
