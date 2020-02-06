# -*- coding: utf-8 -*-

from django.urls import path

from tasks.views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks-home'),
]
