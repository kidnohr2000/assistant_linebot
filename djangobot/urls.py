# -*- coding: utf-8 -*-
# vim:tabstop=4:shiftwidth=4:expandtab

from django.conf.urls import url
# from django.contrib.auth import views as auth_views

from . import views

app_name = 'djangobot'
urlpatterns = [
    url(r'^callback/$', views.JSONView.as_view(), name='callback'),
]
