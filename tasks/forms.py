# -*- coding: utf-8 -*-

from django import forms

from tasks.models import TaskStatus


class TaskStatusForm(forms.ModelForm):
    """TaskStatus form."""

    class Meta(object):
        model = TaskStatus
        fields = ['name']
