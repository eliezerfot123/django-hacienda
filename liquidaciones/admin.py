# -*- coding:utf-8 -*-
from django.contrib import admin
from liquidaciones.models import *

class LiquidacionAdmin(admin.ModelAdmin):
    search_fields = ['numero']
    list_display = ['numero','trimestre','ano','monto','recargo','intereses'
                    ,'impuesto', 'emision']
    ordering = ['numero']
admin.site.register(Liquidacion, LiquidacionAdmin)


class Liquidacion2Admin(admin.ModelAdmin):
    search_fields = ['numero']
    list_display = ['numero', 'deposito', 'contribuyente',
                    'fecha_pago', 'ano', 'modopago',
                    'emision', 'vencimiento', 'liquidador']
    ordering = ['emision']
admin.site.register(Liquidacion2, Liquidacion2Admin)


class ImpuestoAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'descripcion']
    list_display = ['codigo', 'descripcion']
    ordering = ['codigo']
admin.site.register(Impuesto, ImpuestoAdmin)


class PagoAdmin(admin.ModelAdmin):
    search_fields = ['num_liquidacion', 'deposito', 'emision', 'vencimiento', 'observaciones']
    list_display = ['contribuyente', 'num_liquidacion', 'deposito', 'emision', 'vencimiento', 'recargo', 'fecha_pago', 'liquidacion']
    ordering = ['emision']
admin.site.register(Pago, PagoAdmin)


class Pago2Admin(admin.ModelAdmin):
    search_fields = ['liquidacion', 'impuesto']
    list_display = ['liquidacion', 'impuesto', 'ut', 'descuento',
                    'trimestres', 'intereses',
                    'recargo', 'monto']
admin.site.register(Pago2, Pago2Admin)
