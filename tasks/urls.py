# -*- coding: utf-8 -*-

from django.urls import path

from tasks.views import (
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskStatusDeleteView,
    TaskStatusView,
    TaskUpdateView,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks-home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('status/', TaskStatusView.as_view(), name='statuses'),
    path('status/new/', TaskStatusView.as_view(), name='status-create'),
    path(
        'status/<int:pk>/delete/',
        TaskStatusDeleteView.as_view(),
        name='status-delete',
    ),
]
