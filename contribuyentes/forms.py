# -*- coding: utf8 -*-
from django import forms
from django.http import HttpResponseRedirect
from liquidaciones.models import Pago, Liquidacion2, Impuesto, UT
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm, TextInput, Textarea,Select,DateInput

from django.forms.models import ModelChoiceField

from contribuyentes.models import Rubro, Contribuyente,Monto
from liquidaciones.widgets import RubrosWidget,TrimestresWidget,EstimadasWidget
import datetime



class ImpuestosForm(forms.Form):  # [0]
    contrib = forms.CharField(max_length=200, label="Contribuyente", required=True)
    impuesto = forms.ModelChoiceField(queryset=Impuesto.objects.all().order_by('codigo'), required=True, empty_label=None)

    contrib.widget.attrs['class'] = 'ContribAjax col-md-12 form-control span12'
    contrib.widget.attrs['autocomplete'] = 'off'
    contrib.widget.attrs['value'] = ''

    impuesto.widget.attrs['class'] = 'chzn-select span4'
    impuesto.widget.attrs['id'] = 'form-field-select-4'
    impuesto.widget.attrs['multiple'] = ''
    impuesto.widget.attrs['data-placeholder'] = 'Seleccione Impuestos'
    impuesto.widget.attrs['value'] = ''

    def clean_contrib(self):
        data = self.cleaned_data['contrib']
        return Contribuyente.objects.get(id_contrato=data.split(" ")[0])



class RubrosField(ModelChoiceField):
    widget = RubrosWidget

    def save_form_data(self, instance, data):
        pass
    """ Validar la data introducida """
    def clean(self,values,initial=None):
        return  values

class ContribuyenteForm(forms.ModelForm):
    rubro= forms.ModelMultipleChoiceField(queryset=Rubro.objects.all().order_by('codigo'),required=False,label='Rubros')
    rubro.widget.attrs['class'] = 'chzn-select span6 col-md-12 form-control'
    rubro.widget.attrs['multiple'] = ''
    rubro.widget.attrs['data-placeholder'] = 'Seleccione Rubro'
    rubro.widget.attrs['value'] = ''
    direccion=forms.CharField(widget=forms.Textarea)
    direccion.widget.attrs={'class':'autosizejs autosize-transition span4','style':'overflow: hidden; word-wrap: break-word; resize: vertical;'}
    class Meta:
        model=Contribuyente
        exclude=['id_contrato',]
        labels={'cedula_rep':'Cédula del Representante','representante':'Representante legal','direccion':'Dirección','num_identificacion':'Cédula/RIF'  }

class EstimadasField(ModelChoiceField):
    widget= EstimadasWidget
    def save_form_data(self, instance, data):
        pass
    """ Validar la data introducida """
    def clean(self,values,initial=None):
        return  values

class EstimadasForm(forms.Form):  # [1]
    rubros= EstimadasField(queryset=None, label="Rubros", required=True, empty_label=None)
    tipo='EST'
    def procesar(self,wizard,form):
        import datetime
        subtotaldef=0.0
        for ano,rubros in form.cleaned_data['rubros'].iteritems():
            ano=int(ano)
            ut=UT.objects.filter(ano=ano)
            if ut.exists():
                ut=ut[0].valor
            else:
                ut=UT.objects.get(ano=ano-1).valor
            definitivas=Monto.objects.filter(contribuyente=wizard.get_all_cleaned_data()['contrib'],ano=ano)
            if definitivas.exists():
                for montos in rubros:
                    rubro=Rubro.objects.get(codigo=montos)
                    montout=float(rubro.ut)*ut
                    montoali=float(rubros[montos])*(rubro.alicuota/100)
                    if montout>montoali:
                        subtotaldef+=montout
                    else:
                        subtotaldef+=montoali
        return ano,round(subtotaldef,2)

class RubrosForm(forms.Form):  # [1]
    #rubros = forms.ModelChoiceField(queryset=None, label="Rubros", required=True, empty_label=None)

    rubros = RubrosField(queryset=None, label="Rubros", required=True, empty_label=None)
    tipo='DEF'
    #rubros.widget = RubrosWidget()

    """
    def clean_rubros(self):
        subtotales={}
        for (ano,rubros) in self.cleaned_data.get('rubros').iteritems():
            rubro=Rubro.objects.get(id=rubroid)
            montout=float(rubro.ut)*107
            montoali=float(monto)*rubro.alicuota
            if montout>montoali:
                subtotales[rubroid]=montout

            else:
                subtotales[rubroid]=montoali
        for (ano,rubros) in self.cleaned_data.get('rubros').iteritems():
            if '' in rubros.values():
                raise forms.ValidationError('No debe dejar valor vacíos.', code='invalid')
        return subtotales
    """
    def procesar(self,wizard,form):
        subtotaldef=0.0
        for ano,rubros in form.cleaned_data['rubros'].iteritems():
            ano=int(ano)
            if ano ==datetime.datetime.today().year-1:
                ut=UT.objects.filter(ano=ano)
                if ut.exists():
                    ut=ut[0].valor
                else:
                    ut=UT.objects.get(ano=ano-1).valor
                definitivas=Monto.objects.filter(contribuyente=wizard.get_all_cleaned_data()['contrib'],ano=ano)
                if definitivas.exists():
                    for montos in rubros:
                        rubro=Rubro.objects.get(codigo=montos)
                        montout=float(rubro.ut)*ut
                        montoali=float(rubros[montos])*(rubro.alicuota/100)
                        if montout>montoali:
                            subtotaldef+=montout
                        else:
                            subtotaldef+=montoali
                        estimada=definitivas.filter(rubro=rubro).exclude(estimado=None)
                        if estimada.exists():
                            montoali=float(estimada[0].estimado)*(rubro.alicuota/100)
                            if montout>montoali:
                                subtotaldef-=montout
                            else:
                                subtotaldef-=montoali
        return ano,round(subtotaldef,2)


class TrimestresField(ModelChoiceField):
    widget=TrimestresWidget

    #def save_form_data(self, instance, data):
    #    pass
    """ Validar la data introducida """
    def clean(self,values,initial=None):
        return  values


class LiquidacionForm(forms.Form):  # [2]
    trimestre = TrimestresField(queryset=None,required=True,label="")
    deposito = forms.CharField(label="Nro. Vauche", max_length="20", required=True)
    choices_modopago = (('CH','Cheque'),('DP','Deposito'),('TF','Transferencia'))
    modopago = forms.ChoiceField(choices=choices_modopago, required=True, label="Tipo de Pago")
    observaciones = forms.CharField(widget=forms.Textarea, required=True)

    deposito.widget.attrs['class'] = 'span6'
    deposito.widget.attrs['placeholder'] = 'Ingrese Número de Cheque'
    deposito.widget.attrs['autocomplete'] = 'off'
    deposito.widget.attrs['required'] = 'required'
    observaciones.widget.attrs['class'] = 'autosize-transition span6'
    observaciones.widget.attrs['style'] = 'height:60px;'
    observaciones.widget.attrs['placeholder'] = 'Observaciones de la liquidación'
    observaciones.widget.attrs['required'] = 'required'

    def clean_deposito(self):
        if self.data['4-deposito'] == '':
            raise forms.ValidationError("Debe colocar el numero del vauche.")
        else:
            return self.data['4-deposito']

    def clean_observaciones(self):
        if self.data['4-observaciones'] == '':
            raise forms.ValidationError("Debe colocar una(as) observacion(es).")
        else:
            return self.data['4-observaciones']


class EditarContribuyenteForm(forms.ModelForm):
    rubro = forms.ModelMultipleChoiceField(queryset=Rubro.objects.all().order_by('codigo'), required=False, label='Rubros')
    rubro.widget.attrs['class'] = 'chzn-select span6 col-md-12 form-control'
    rubro.widget.attrs['multiple'] = ''
    rubro.widget.attrs['data-placeholder'] = 'Seleccione Rubros...'
    rubro.widget.attrs['value'] = ''

    class Meta:
        model = Contribuyente
        exclude = ['id_contrato',]
        labels = {'cedula_rep':'Cédula del Representante','representante':'Representante legal','direccion':'Dirección','num_identificacion':'Cédula/RIF'}
        widgets = {
            'representante': TextInput(attrs={'autofocus':'autofocus', 'class': 'span6'}),
            'nombre': TextInput(attrs={'autofocus':'autofocus', 'class': 'span6'}),
            'direccion': Textarea(attrs={'autofocus':'autofocus', 'class': 'autosize-transition span8 limited', 'maxlength': '200', 'data-maxlength': '200', 'style': 'height:60px;'}),
        }
