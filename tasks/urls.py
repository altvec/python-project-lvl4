# -*- coding: utf-8 -*-

from django.urls import path

from tasks.views import TaskCreateView, TaskDetailView, TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks-home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
]
