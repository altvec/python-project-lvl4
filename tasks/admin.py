# -*- coding: utf-8 -*-

from django.contrib import admin

from tasks.models import Tag, Task, TaskStatus


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Display tasks in admin interface."""

    list_display = ('name', 'description', 'status', 'creator', 'assigned_to')
    list_filter = ('status',)
    search_fileds = ('name', 'description')


admin.site.register(Tag)
admin.site.register(TaskStatus)
