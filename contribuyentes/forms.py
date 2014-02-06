# -*- coding: utf8 -*-
from django import forms
from django.http import HttpResponseRedirect
from liquidaciones.models import Pago, Liquidacion, Impuesto
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm, TextInput, Textarea,Select,DateInput


class ImpuestosForm(forms.Form):  # [0]
    contrib = forms.CharField(label="Contribuyente")
    impuesto = forms.ModelChoiceField(queryset=Impuesto.objects.all().order_by('codigo'), required=True)

    def clean(self):
        try:
            self.cleaned_data
        except:
            return forms.ValidationError('Debe seleccionar un contribuyente y unos rubros.')
        else:
            return self.cleaned_data

class RubrosForm(forms.Form):  # [1]
    rubros = forms.ModelChoiceField(queryset=None, required=True)


class LiquidacionForm(forms.Form):  # [2]
    nDeposito = forms.IntegerField()
    observaciones = forms.CharField(widget=forms.Textarea)
    trimestres = forms.IntegerField()
