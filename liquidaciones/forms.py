# -*- coding: utf8 -*-
from django import forms
from liquidaciones.models import Pago

class PagoForm(forms.Form):
    contrib=forms.CharField()

