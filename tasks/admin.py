# -*- coding: utf-8 -*-

from django.contrib import admin  # noqa: F401

# Register your models here.
from .models import Task, Tag

admin.site.register(Task)
admin.site.register(Tag)
