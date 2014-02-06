from django.conf.urls import patterns, include, url
from contribuyentes.forms import *
from contribuyentes.views import LiquidacionWizard


urlpatterns = patterns('',
    url(r'^liquidaciones/(\d+)/$', 'contribuyentes.views.contrib_liquids', name="contrib-liquids"),
    url(r'^crear_pago/$', 'contribuyentes.views.crear_pagos', name="crear_pago"),
    url(r'^ajax_contrib/$', 'contribuyentes.views.ajax_contrib', name="ajax_contrib"),
    url(r'^$', LiquidacionWizard.as_view([ImpuestosForm, RubrosForm, LiquidacionForm]), name="cargar-liquid")(request),
)
