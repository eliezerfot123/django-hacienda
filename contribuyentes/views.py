# -*- coding: utf-8 -*-
from django.shortcuts import render
from contribuyentes.models import *
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from liquidaciones.models import Pago, Liquidacion,Impuesto
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
import json
from django.contrib.formtools.wizard.views import SessionWizardView
from contribuyentes.forms import ImpuestosForm, RubrosForm, LiquidacionForm


class LiquidacionWizard(SessionWizardView):
    form_list = [ImpuestosForm, RubrosForm, LiquidacionForm]
    template_name = 'crear_pago.html'
    contrib=None
    impuesto=None
    query=None
    montos=None


    def get_form(self, step=None, data=None, files=None):
        formu = super(LiquidacionWizard, self).get_form(step, data, files)

        if step is None:
            step = self.steps.current

        if step == '1' :
            formu.fields['rubros'].queryset = self.query
        elif step=='2' :
            formu.fields['trimestre'].choices=[self.montos]

        return formu
    def process_step(self, form):


        if self.steps.current == '0':
            self.contrib = form.cleaned_data['contrib']
            self.impuesto = form.cleaned_data['impuesto']
            self.query = Rubro.objects.filter(contribuyente__num_identificacion=self.contrib.split(" ")[1])

        elif self.steps.current == '1':
            subtotal=0.0
            for rubroid,subtotales in form.cleaned_data['rubros'].iteritems():
                subtotal+=float(subtotales)
            self.montos = dict({'impuesto':self.get_all_cleaned_data()['impuesto'],'montos':subtotal})

        return self.get_form_step_data(form)

    def done(self, form_list, **kwargs):
        do_something_with_the_form_data(form_list)
        return render(request, 'crear_pago.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


@login_required(login_url='/login/')
def lista_contribuyentes(request):
    if request.method == 'GET':
        contribuyente = request.GET.get('contrib')
        if contribuyente is not None:
            contrib_filters = Contribuyente.objects.filter(
                Q(id_contrato__icontains=contribuyente) |
                Q(num_identificacion__startswith=contribuyente) |
                Q(nombre__icontains=contribuyente) |
                Q(telf__startswith=contribuyente) |
                Q(email__icontains=contribuyente) |
                Q(representante__icontains=contribuyente) |
                Q(cedula_rep__startswith=contribuyente)).order_by('-nombre')

            return render(request, 'lista_contribuyentes.html',
                          {'contrib_filters': contrib_filters,
                           'usuario': request.user.get_username()},
                          context_instance=RequestContext(request))
        else:
            return render(request, 'lista_contribuyentes.html',
                          {'usuario': request.user.get_username()})

    return render(request, 'lista_contribuyentes.html')


@login_required(login_url='/login/')
def contrib_liquids(request, id_contrib):
    if id_contrib is not None:
        contrib_liq = Contribuyente.objects.get(pk=id_contrib).liquidaciones(id_contrib)
        contrib_representante = Contribuyente.objects.get(pk=id_contrib)

        return render(request, 'contrib_liquidaciones.html',
                    {'contrib_liq': contrib_liq,
                     'contrib_representante': contrib_representante,
                    'usuario': request.user.get_username()},
                    context_instance=RequestContext(request))
    else:
        return render(request, 'contrib_liquidaciones.html',
                    {'usuario': request.user.get_username()})

    return render(request, 'contrib_liquidaciones.html')


@login_required(login_url='/login/')
@csrf_protect
def ajax_contrib(request):
    if request.method == 'GET':
        contribuyente = request.GET.get('query')
        if contribuyente is not None:
            contrib_filter = Contribuyente.objects.filter(
                Q(id_contrato__icontains=contribuyente) |
                Q(num_identificacion__startswith=contribuyente) |
                Q(nombre__icontains=contribuyente) |
                Q(telf__startswith=contribuyente) |
                Q(email__icontains=contribuyente) |
                Q(representante__icontains=contribuyente) |
                Q(cedula_rep__istartswith=contribuyente)).values_list('pk','id_contrato','num_identificacion','nombre').order_by('-nombre')

    contrib=[({'id':p[0], 'nombre': u'{0} {1} {2}'.format( p[1], p[2],p[3]),}) for p in contrib_filter]
    contrib_json = json.dumps(contrib)
    return HttpResponse(contrib_json, mimetype='application/javascript')
