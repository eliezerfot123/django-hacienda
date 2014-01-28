# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login,logout


urlpatterns = patterns('',
    url(r'logout/',logout,{'next_page':'/login'},),
    url(r'^.*$', 'login.views.home', name='home'),
)
