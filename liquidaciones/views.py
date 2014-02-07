from django.shortcuts import render
from django.views.generic import *
from liquidaciones.models import *
from liquidaciones.forms import PagoForm
from liquidaciones.models import Pago
from django.utils import simplejson as json
from django import http
from django.db.models import Q


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json([obj.as_dict() for obj in self.get_queryset()]))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

class PagoView(FormView):
    form_class=PagoForm
    template_name = 'pagos_registrar.html'

class LiquidacionJSON(JSONResponseMixin,ListView):

    def get_queryset(self,):
        query=self.request.GET['query']
        return Liquidacion.objects.filter(Q(Q(numero__istartswith=query)|Q(pago__contribuyente__num_identificacion__icontains=query)|Q(pago__contribuyente__id_contrato__istartswith=query)),Q(pago__fecha_pago=None))

