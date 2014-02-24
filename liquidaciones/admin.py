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

    def pagos2(self, obj):
        pagos=[str(pago['cancelado']) for pago in obj.pago2_set.all().values('cancelado')]
        return ("%s  " % (', '.join(pagos) ))
    search_fields = ['numero']
    list_display = ('numero', 'deposito', 'contribuyente',
                    'fecha_pago', 'ano', 'modopago',
                    'emision', 'vencimiento', 'liquidador','pagos2')
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


class UTAdmin(admin.ModelAdmin):
    search_fields = ['ano', 'valor']
    list_display = ['ano', 'valor']
admin.site.register(UT, UTAdmin)
