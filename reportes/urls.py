from django.conf.urls import patterns, include, url
from reportes.views import *

urlpatterns = patterns('',
    url(r'^licencia_alcohol/$', 'reportes.views.licencia_expendio_alcohol'),
)
