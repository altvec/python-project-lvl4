# -*- coding: utf-8 -*-

import django_filters
from taggit.forms import TagField

from tasks.models import Task


class TagFilter(django_filters.CharFilter):
    """Filter for tags."""

    field_class = TagField

    def __init__(self, *args, **kwargs):  # noqa: D107
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, **kwargs)


class TaskFilter(django_filters.FilterSet):
    """Filter for tasks."""

    tags = TagFilter(field_name='tags__name')

    class Meta(object):
        model = Task
        fields = ('creator', 'status', 'assigned_to', 'tags')
