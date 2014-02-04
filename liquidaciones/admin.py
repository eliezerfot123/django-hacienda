# -*- coding:utf-8 -*-
from django.contrib import admin
from liquidaciones.models import *

class LiquidacionAdmin(admin.ModelAdmin):
    search_fields = ['numero']
    list_display = ['numero','trimestre','ano','monto','recargo','intereses'
                    ,'impuesto', 'emision']
    ordering = ['numero']
admin.site.register(Liquidacion, LiquidacionAdmin)


class ImpuestoAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'descripcion']
    list_display = ['codigo', 'descripcion']
    ordering = ['codigo']
admin.site.register(Impuesto, ImpuestoAdmin)


class PagoAdmin(admin.ModelAdmin):
    search_fields = ['deposito', 'emision', 'vencimiento', 'observaciones']
    list_display = ['deposito', 'emision', 'vencimiento', 'recargo', 'fecha_pago', 'liquidacion', 'contribuyente']
    ordering = ['emision']
admin.site.register(Pago, PagoAdmin)
