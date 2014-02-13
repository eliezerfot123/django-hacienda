from django.conf.urls import patterns, include, url
from contribuyentes.forms import *
from contribuyentes.views import LiquidacionWizard, ContribuyenteCrear, ContribuyenteEditar
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^liquidaciones/(\d+)/$', 'contribuyentes.views.contrib_liquids', name="contrib-liquids"),
    url(r'^ajax_contrib/$', 'contribuyentes.views.ajax_contrib', name="ajax_contrib"),
    url(r'^agregar/$',ContribuyenteCrear.as_view(),name='crear_contrib'),
    url(r'^editar/(?P<pk>\d+)/$',ContribuyenteEditar.as_view(),name='editar_contrib'),
    url(r'crear_pago/$', login_required(LiquidacionWizard.as_view([
                            ImpuestosForm, RubrosForm,
                            LiquidacionForm]), login_url='/login/'), name="cargar-liquid"),
    url(r'crear_estimada/$', login_required(LiquidacionWizard.as_view([
                            ImpuestosForm, EstimadasForm,
                            LiquidacionForm]), login_url='/login/'), name="cargar-estim"),
)
