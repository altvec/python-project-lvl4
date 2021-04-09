# -*- coding: utf-8 -*-

from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks-home'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('task/new/', views.TaskCreate.as_view(), name='task-create'),
    path(
        'task/<int:pk>/update/',
        views.TaskUpdate.as_view(),
        name='task-update',
    ),
    path(
        'task/<int:pk>/delete/',
        views.TaskDelete.as_view(),
        name='task-delete',
    ),
    path('status/', views.TaskStatusList.as_view(), name='statuses'),
    path('status/new/', views.TaskStatusList.as_view(), name='status-create'),
    path(
        'status/<int:pk>/delete/',
        views.TaskStatusDelete.as_view(),
        name='status-delete',
    ),
    path(
        'status/<int:pk>/update/',
        views.TaskStatusUpdate.as_view(),
        name='status-update',
    ),
]
