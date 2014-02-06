# -*- coding: utf8 -*-
from django import forms
from django.http import HttpResponseRedirect
from liquidaciones.models import Pago, Liquidacion, Impuesto
from django.core.exceptions import ValidationError
from django.db.models import Q


class ImpuestosForm(forms.Form):  # [0]
    impuesto = forms.ModelChoiceField(queryset=Impuesto.objects.all().order_by('codigo'), required=True)
    contrib = forms.CharField(label="Contribuyente")


class RubrosForm(forms.Form):  # [1]
    rubros = forms.ModelChoiceField(queryset=None, required=True)


class LiquidacionForm(forms.Form):  # [2]
    nDeposito = forms.IntegerField()
    fecha_pago = forms.DateField()
    observaciones = forms.CharField(widget=forms.Textarea)
    trimestres = forms.IntegerField()
