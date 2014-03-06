from django.conf.urls import patterns, include, url
from contribuyentes.forms import *
from contribuyentes.views import LiquidacionWizard, ContribuyenteCrear, ContribuyenteEditar,actividad_eco,definitiva,estimada,crear_estimada
from liquidaciones.forms import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^liquidaciones/(\d+)/$', 'contribuyentes.views.contrib_liquids', name="contrib-liquids"),
    url(r'^ajax_contrib/$', 'contribuyentes.views.ajax_contrib', name="ajax_contrib"),
    url(r'^agregar/$',ContribuyenteCrear.as_view(),name='crear_contrib'),
    url(r'^editar/(?P<pk>\d+)/$',ContribuyenteEditar.as_view(),name='editar_contrib'),
    url(r'crear_pago/$', login_required(LiquidacionWizard.as_view([ ImpuestosForm, TipoLiqEconomica, AgregarEstimadoForm,RubrosForm,EstimadasForm, LiquidacionForm],condition_dict={'1':actividad_eco,'2':crear_estimada,'3':definitiva,'4':estimada}), login_url='/login/'), name="cargar-liquid"),
    url(r'crear_estimada/$', login_required(LiquidacionWizard.as_view([
                            ImpuestosForm, AgregarEstimadoForm,  EstimadasForm,
                            LiquidacionForm]), login_url='/login/'), name="cargar-estim"),
)
