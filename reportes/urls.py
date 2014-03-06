from django.conf.urls import patterns, include, url
from reportes.views import *

urlpatterns = patterns('',
    url(r'^licencia_alcohol/$', 'reportes.views.licencia_expendio_alcohol'),
    url(r'^vauches/$', 'reportes.views.vauche_imprimir'),
    url(r'^liquidacion/(\w+)/$', 'reportes.views.liquidacion_report'),
    url(r'^boletin_def/(\w+)/$', 'reportes.views.boletin_liquid_definitiva'),
    url(r'^boletin_est/(\w+)/$', 'reportes.views.boletin_liquid_estimada'),
)
