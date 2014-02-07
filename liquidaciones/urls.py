from django.conf.urls import patterns, include, url
from liquidaciones.views import *
urlpatterns = patterns('',
    url(r'pagos/$', PagoView.as_view(), name="gestionar_pago"),
    url(r'json/', LiquidacionJSON.as_view(), name="ajax_liquidacion"),

)
