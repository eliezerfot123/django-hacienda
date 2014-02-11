from django.conf.urls import patterns, include, url
from liquidaciones.views import *
from django.contrib.auth.decorators import login_required
urlpatterns = patterns('',
    url(r'pagos/$', login_required(PagoView.as_view()), name="gestionar_pago"),
    url(r'json/', login_required(LiquidacionJSON.as_view()), name="ajax_liquidacion"),

)
