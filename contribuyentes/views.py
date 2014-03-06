# -*- coding: utf-8 -*-
from django.shortcuts import render
from contribuyentes.models import *
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from liquidaciones.models import Pago, Liquidacion,Impuesto,Liquidacion2,Pago2,UT
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
import json
from django.contrib.formtools.wizard.views import SessionWizardView
from contribuyentes.forms import ImpuestosForm, RubrosForm, LiquidacionForm,ContribuyenteForm, EditarContribuyenteForm
from django.views.generic.edit import CreateView, UpdateView
from contribuyentes.models import Contribuyente,Credito
from django.db import transaction
import datetime
from django.core.urlresolvers import reverse


class ContribuyenteCrear(CreateView):
    model=Contribuyente
    template_name = 'contribuyente_crear.html'
    form_class=ContribuyenteForm
    success_url='.'
    def form_valid(self,form):
        from django.contrib import messages
        messages.success(self.request, "Contribuyente registrado")

        return super(ContribuyenteCrear,self).form_valid(form)


class ContribuyenteEditar(UpdateView):
    model = Contribuyente
    template_name = 'contribuyente_editar.html'
    form_class = EditarContribuyenteForm
    success_url = '.'

    def form_valid(self,form):
        from django.contrib import messages
        messages.success(self.request, "Contribuyente Actualizado")

        return super(ContribuyenteEditar, self).form_valid(form)


def actividad_eco(wizard):
    if wizard.get_cleaned_data_for_step('0'):
        return wizard.get_cleaned_data_for_step('0')['impuesto'].codigo==301020700
def definitiva(wizard):
    if wizard.get_cleaned_data_for_step('1'):
        return wizard.get_cleaned_data_for_step('1').get('tipo_liquidacion')=='def'

def crear_estimada(wizard):
    if wizard.get_cleaned_data_for_step('0'):
        return  not Monto.objects.filter(contribuyente=wizard.get_cleaned_data_for_step('0')['contrib'],ano=datetime.date.today().year).exclude(estimado=None).exists() or wizard.get_cleaned_data_for_step('2')

    

def estimada(wizard):
    if wizard.get_cleaned_data_for_step('1'):
        return wizard.get_cleaned_data_for_step('1').get('tipo_liquidacion')=='est'

class LiquidacionWizard(SessionWizardView):
    template_name = 'crear_pago.html'
    contrib=None
    impuesto=None
    query=None
    montos=None

    def get_form(self, step=None, data=None, files=None):
        formu = super(LiquidacionWizard, self).get_form(step, data, files)
        if step is None:
            step = self.steps.current
        if step == '2' and 'estimado' in formu.fields :
            contribuyente=self.get_cleaned_data_for_step('0')['contrib']
            if not Monto.objects.filter(contribuyente=contribuyente,ano=datetime.date.today().year).exclude(estimado=None).exists():
                formu.fields['estimado'].queryset=contribuyente.rubro.all()

            else:
                step='4'
                formu = super(LiquidacionWizard, self).get_form(step, data, files)
        if 'rubros' in formu.fields:
            formu = super(LiquidacionWizard, self).get_form(step, data, files)
            contribuyente=self.get_cleaned_data_for_step('0')['contrib']
            formu = super(LiquidacionWizard, self).get_form(step, data, files)
            formu.fields['rubros'].queryset = Monto.objects.filter(contribuyente=contribuyente)

        elif 'trimestre' in formu.fields :
            formu.fields['trimestre'].choices=[self.montos]

        print step;
        return formu

    @transaction.atomic
    def process_step(self, form):
        import datetime
        if self.steps.current == '0':
            self.impuesto = form.cleaned_data['impuesto']
            self.query = Monto.objects.filter(contribuyente=form.cleaned_data['contrib'])
        if 'procesar' in dir(form): 
            subtotaldef=0.0
            subtotalest=0.0
            if form.is_valid():
                ano,subtotaldef=form.procesar(self,form)
                """
                elif ano==datetime.datetime.today().year:
                    estimadas=Monto.objects.filter(contribuyente=self.get_all_cleaned_data()['contrib'],ano=ano).exclude(estimado=None)
                    if estimadas.exists():
                        ut=UT.objects.filter(ano=ano)
                        if ut.exists():
                            ut=ut[0].valor
                        else:
                            ut=UT.objects.get(ano=ano-1).valor
                        for montos in rubros:
                            rubro=Rubro.objects.get(codigo=montos)
                            montout=float(rubro.ut)*ut
                            montoali=float(rubros[montos])*(rubro.alicuota/100)
                            if montout>montoali:
                                subtotalest+=montout
                            else:
                                subtotalest+=montoali

                """
                self.montos = dict({'impuesto':self.get_cleaned_data_for_step('0')['impuesto'],'montos':{ano:subtotaldef},'contribuyente':self.get_cleaned_data_for_step('0')['contrib']})
            else:
                formu.fields['rubros'].queryset = self.query
        elif 'estimado' in form.cleaned_data:
            contribuyente=self.get_cleaned_data_for_step('0')['contrib']
            for ano in form.cleaned_data['estimado']:
                for rubroid in form.cleaned_data['estimado'][ano]:
                    rubro=Rubro.objects.get(codigo=rubroid)
                    Monto.objects.get_or_create(contribuyente=contribuyente,rubro=rubro,estimado=form.cleaned_data['estimado'][ano][rubroid],ano=ano)
        return self.get_form_step_data(form)

    def render_next_step(self, form, **kwargs):
        if self.steps.current == '1':
            if self.get_cleaned_data_for_step('1')['tipo_liquidacion'] == 'est':
                filter_liquid = Liquidacion2.objects.filter(ano=datetime.datetime.today().year, contribuyente=self.get_cleaned_data_for_step('0')['contrib'].id, pago2__impuesto=self.get_cleaned_data_for_step('0')['impuesto'].id)
                """Validación para comprobar si ya se a creado la estimada"""
                if filter_liquid:
                    from django.contrib import messages
                    messages.error(self.request, "%s en el año %s" % (self.get_cleaned_data_for_step('0')['impuesto'], datetime.datetime.today().year))
                    return HttpResponseRedirect(reverse('contrib-liquids', args=[self.get_cleaned_data_for_step('0')['contrib'].id]))
        return super(LiquidacionWizard, self).render_next_step(form, **kwargs)


    @transaction.atomic
    def done(self, form_list, **kwargs):
        #do_something_with_the_form_data(form_list)
        import calendar
        import datetime
        for formu in form_list:
            if 'tipo' in dir(formu):
                tipo=formu.tipo
                break
        liquidacion=Liquidacion2(ano=self.get_all_cleaned_data()['trimestre'].values()[0].keys()[0],
        deposito=self.get_all_cleaned_data()['numero'],
        emision=datetime.date.today(),
        contribuyente=self.get_all_cleaned_data()['contrib'],
        vencimiento= datetime.date(datetime.date.today().year,
        datetime.date.today().month,calendar.monthrange(datetime.date.today().year, datetime.date.today().month)[1]),
        observaciones=self.get_all_cleaned_data()['observaciones'],
        liquidador=self.request.user,tipo=tipo,
        modopago=self.get_all_cleaned_data()['modopago'])

        liquidacion.save()

        for ano,rubros in self.get_all_cleaned_data()['rubros'].iteritems():
            monto=Monto.objects.filter(contribuyente=self.get_all_cleaned_data()['contrib'],ano=ano,definitivo=None)
            for montos in rubros:
                definitiva=monto.filter(rubro__codigo=montos)
                if definitiva.exists():
                    definitiva=definitiva[0]
                    definitiva.definitivo=rubros[montos]
                    definitiva.save()

        for impuesto,pagos in self.get_all_cleaned_data()['trimestre'].iteritems():
            ut=UT.objects.filter(ano=datetime.date.today().year-1)[0]
            pagos=pagos.values()[0]
            if float(pagos['monto'])<0:
                credito=abs(float(pagos['monto']))
            else:
                credito=0.0

                """ Busca de credito fiscal """
            credit,creado=Credito.objects.get_or_create(contribuyente=self.get_all_cleaned_data()['contrib'])
            credit.monto=credito
            credit.save()
            if liquidacion.tipo=='DEF':
                credito=0.0

            pago=Pago2(liquidacion=liquidacion,impuesto=Impuesto.objects.get(codigo=impuesto),descuento=pagos['descuento'],trimestres=pagos['trimestres'],monto=pagos['monto'],cancelado=pagos['cancelado'],intereses=pagos['intereses'],recargo=pagos['recargo'],ut=ut,credito_fiscal=pagos['credito'])
            pago.save()

        return render(self.request, 'liquid_cargada.html', {
            'liquid_numero': liquidacion.numero, 'tipo_liquid': self.get_cleaned_data_for_step('1')['tipo_liquidacion'],
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
