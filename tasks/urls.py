# -*- coding: utf-8 -*-

from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
]
