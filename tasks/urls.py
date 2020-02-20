# -*- coding: utf-8 -*-

from django.urls import path

from tasks.views import (
    TaskCreate,
    TaskDelete,
    TaskDetail,
    TaskList,
    TaskStatusDelete,
    TaskStatusList,
    TaskStatusUpdate,
    TaskUpdate,
)

urlpatterns = [
    path('', TaskList.as_view(), name='tasks-home'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task/new/', TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdate.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
    path('status/', TaskStatusList.as_view(), name='statuses'),
    path('status/new/', TaskStatusList.as_view(), name='status-create'),
    path(
        'status/<int:pk>/delete/',
        TaskStatusDelete.as_view(),
        name='status-delete',
    ),
    path(
        'status/<int:pk>/update/',
        TaskStatusUpdate.as_view(),
        name='status-update',
    ),
]
