# -*- coding:utf-8 -*-
from django.contrib import admin
from django.conf import settings
from contribuyentes.models import *

class ContribuyenteAdmin(admin.ModelAdmin):
    search_fields = ['id_contrato','num_identificacion','nombre','representante','cedula_rep']
    list_display = ['id_contrato','num_identificacion','nombre','telf','email','representante','cedula_rep']
    ordering = ['id_contrato']
admin.site.register(Contribuyente, ContribuyenteAdmin)

class RubroAdmin(admin.ModelAdmin):
    search_fields = ['codigo','rubro','ut']
    list_display = ['codigo','rubro','alicuota','ut']
    ordering = ['codigo']
admin.site.register(Rubro, RubroAdmin)

class LicenciaAdmin(admin.ModelAdmin):
    search_fields = ['serial', 'control', 'numero']
    list_display = ['serial','control', 'numero', 'cantidad', 'emision', 'valido', 'contribuyente']
    ordering = ['serial']
admin.site.register(Licencia, LicenciaAdmin)
