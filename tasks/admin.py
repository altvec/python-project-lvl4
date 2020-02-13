# -*- coding: utf-8 -*-

from django.contrib import admin

from tasks.models import Tag, Task, TaskStatus


class TaskAdmin(admin.ModelAdmin):
    """Display tasks in admin interface."""

    list_display = ('name', 'description', 'status', 'creator', 'assigned_to')


admin.site.register(Tag)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskStatus)
