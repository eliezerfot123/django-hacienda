# -*- coding: utf-8 -*-
from django.shortcuts import render
from contribuyentes.models import *
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from liquidaciones.models import Pago, Liquidacion,Impuesto
from contribuyentes.forms import CrearPagosForm
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.utils import simplejson
import json


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
def crear_pagos(request):
    if request.method == 'POST':
        form = CrearPagosForm(request.POST)
        if form.is_valid():

            pass
        else:
            return render(request, 'crear_pago.html',)

    else:
        form = CrearPagosForm()
        c = {}
        impuestos=Impuesto.objects.all()
        c.update(csrf(request))
        c.update({'form':form, 'usuario':request.user.get_username(),'impuestos':impuestos})
        return render(request, 'crear_pago.html', c)


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
                Q(cedula_rep__startswith=contribuyente)).order_by('-nombre')

    contrib_json = simplejson.dumps({'result':list(contrib_filter)})
    return HttpResponse(contrib_json, mimetype='application/javascript')
