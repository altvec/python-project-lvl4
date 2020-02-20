# -*- coding: utf-8 -*-

from django import forms

from tasks.models import Task, TaskStatus


class TaskForm(forms.ModelForm):
    """Task form."""

    class Meta(object):
        model = Task
        fields = [
            'name',
            'description',
            'tags',
            'creator',
            'assigned_to',
            'status',
        ]


class TaskStatusForm(forms.ModelForm):
    """TaskStatus form."""

    class Meta(object):
        model = TaskStatus
        fields = ['name']
