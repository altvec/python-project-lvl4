# -*- coding: utf-8 -*-

from django.contrib import admin  # noqa: F401

from tasks.models import Tag, Task

admin.site.register(Tag)
admin.site.register(Task)
