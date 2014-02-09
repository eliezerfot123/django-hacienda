# -*- coding: utf8 -*-
from django import forms
from liquidaciones.models import Pago2,Liquidacion2

class PagoForm(forms.Form):
    liquidacion=forms.CharField(label="Nro. Liquidación")
    liquidacion.widget.attrs['class']='col-md-3 form-control span3'
    liquidacion.widget.attrs['id'] = 'PagosAjax'
    liquidacion.widget.attrs['autocomplete'] = 'off'
    liquidacion.widget.attrs['value'] = ''
    fecha=forms.CharField()
    fecha.widget.attrs['class']='span3 date-picker'
    fecha.widget.attrs['data-date-format']='dd-mm-yyyy'
    fecha.widget.attrs['autocomplete'] = 'off'
    fecha.widget.attrs['value'] = ''
    def clean_liquidacion(self):
        return Liquidacion2.objects.get(numero=self.cleaned_data['liquidacion'].split()[0])
    def clean_fecha(self):
        fecha=self.cleaned_data['fecha'].split('-')
        return fecha[2]+'-'+fecha[1]+'-'+fecha[0]
        

