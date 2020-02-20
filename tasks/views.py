# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.views.generic.edit import FormMixin

from tasks.forms import TaskStatusForm
from tasks.models import Task, TaskStatus


class TaskListView(ListView):
    """A view for list of tasks."""

    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'
    ordering = ['-pk']

    def get_queryset(self):
        """Filter by tag if it is provided in GET parameters."""
        queryset = Task.objects.all()
        if self.request.GET.get('tags'):
            queryset = queryset.filter(tags=self.request.GET.get('tags'))
        return queryset


class TaskDetailView(DetailView):
    """Task details view."""

    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Task create view."""

    model = Task
    fields = ['name', 'description', 'tags', 'assigned_to', 'status']
    template_name = 'task_create.html'
    success_url = reverse_lazy('tasks-home')
    success_message = 'Task %(name)s was created successfully.'

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


class TaskStatusView(FormMixin, ListView):
    """A view for task statuses."""

    model = TaskStatus
    template_name = 'task_statuses.html'
    form_class = TaskStatusForm
    context_object_name = 'statuses'

    def get_success_url(self):  # noqa: D102
        return reverse_lazy('statuses')

    def get_queryset(self):  # noqa: D102
        return TaskStatus.objects.all()

    def post(self, request, *args, **kwargs):  # noqa: D102
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):  # noqa: D102
        TaskStatus.objects.create(name=form.cleaned_data['name'])
        return super().form_valid(form)


class TaskStatusDeleteView(LoginRequiredMixin, DeleteView):
    """TaskStatus delete view."""

    model = TaskStatus
    success_url = reverse_lazy('statuses')
    template_name = 'taskstatus_confirm_delete.html'


class TaskStatusUpdateView(LoginRequiredMixin, UpdateView):
    """TaskStatus update view."""

    model = TaskStatus
    fields = ['name']
    template_name = 'taskstatus_edit.html'

    def form_valid(self, form):
        """Validate form."""
        form.instance.creator = self.request.user
        return super().form_valid(form)
