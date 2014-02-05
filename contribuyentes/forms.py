# -*- coding: utf8 -*-
from django import forms
from django.http import HttpResponseRedirect
from liquidaciones.models import Pago, Liquidacion
from django.core.exceptions import ValidationError
from django.db.models import Q


class CrearPagosForm(forms.ModelForm):
    liquidacion = forms.ModelChoiceField(queryset=None, required=True)

    class Meta:
        model = Pago
        fields = ['liquidacion', 'contribuyente', 'deposito',
                  'fecha_pago', 'observaciones']
