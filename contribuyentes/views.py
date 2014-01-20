# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from contribuyentes.models import *
from django.template.context import RequestContext

def lista_contribuyentes(request):
    contrib = Contribuyente.objects.all().order_by('-nombre')
    return render(request, 'lista_contribuyentes.html', {'contribuyentes':contrib}, 
    	context_instance = RequestContext(request))

