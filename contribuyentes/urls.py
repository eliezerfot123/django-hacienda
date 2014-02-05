from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^liquidaciones/(\d+)/$', 'contribuyentes.views.contrib_liquids', name="contrib-liquids"),
    url(r'^crear_pago/$', 'contribuyentes.views.crear_pagos', name="crear_pago"),
    url(r'^ajax_contrib/$', 'contribuyentes.views.ajax_contrib', name="ajax_contrib"),
)
