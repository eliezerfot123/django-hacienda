# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from contribuyentes.models import *
from django.template.context import RequestContext
from django.db.models import Q

def lista_contribuyentes(request):
	if request.method == 'GET':
		contribuyente = request.GET.get('contrib')
		if contribuyente is not None:
			contrib_filters = Contribuyente.objects.filter(
				Q(id_contrato__icontains=contribuyente) | Q(num_identificacion__startswith=contribuyente) |
				Q(nombre__icontains=contribuyente) | Q(telf__startswith=contribuyente) |
				Q(email__icontains=contribuyente) | Q(representante__icontains=contribuyente) |
				Q(cedula_rep__startswith=contribuyente)).order_by('-nombre')

			return render(request, 'lista_contribuyentes.html', {'contrib_filters':contrib_filters},
				context_instance = RequestContext(request))
		else:
			return render(request, 'lista_contribuyentes.html')
    
	return render(request, 'lista_contribuyentes.html')
