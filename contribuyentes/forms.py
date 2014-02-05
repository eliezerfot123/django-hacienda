# -*- coding: utf8 -*-
from django import forms
from django.http import HttpResponseRedirect
from liquidaciones.models import Pago
from django.core.exceptions import ValidationError
from django.db.models import Q


class CrearPagosForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['num_liquidacion', 'deposito', 'emision', 'vencimiento', 'fecha_pago', 'credito_fiscal', 'descuento', 'impuesto', 'recargo', 'intereses', 'observaciones']
