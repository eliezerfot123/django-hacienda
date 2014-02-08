# -*- coding: utf8 -*-
from django import forms
from django.http import HttpResponseRedirect
from liquidaciones.models import Pago, Liquidacion, Impuesto
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm, TextInput, Textarea,Select,DateInput

from django.forms.models import ModelChoiceField

from contribuyentes.models import Rubro,Contribuyente


class ImpuestosForm(forms.Form):  # [0]
    contrib = forms.CharField(max_length=200, label="Contribuyente", required=True)
    impuesto = forms.ModelChoiceField(queryset=Impuesto.objects.all().order_by('codigo'), required=True)

    contrib.widget.attrs['class'] = 'ContribAjax col-md-12 form-control span12'
    contrib.widget.attrs['autocomplete'] = 'off'
    contrib.widget.attrs['value'] = ''

    impuesto.widget.attrs['class'] = 'chzn-select span4'
    impuesto.widget.attrs['id'] = 'form-field-select-4'
    impuesto.widget.attrs['multiple'] = ''
    impuesto.widget.attrs['data-placeholder'] = 'Seleccione Impuestos'
    impuesto.widget.attrs['value'] = ''
    def clean_contrib(self):
        data=self.cleaned_data['contrib']
        return Contribuyente.objects.get(num_identificacion=data.split(" ")[1])


"""Widget Rubros"""
class RubrosWidget(forms.widgets.Select):
    attrs = {}

    def __init__(self, attrs=None, choices=()):
        super(RubrosWidget, self).__init__(attrs)
        self.choices = list(choices)
    """ Retorna la data introducida en forma de diccionario"""
    def value_from_datadict(self, data, files, name):
        import string
        rubros = {}
        for campo, valor in data.iteritems():
            if campo.find('rubro-') > -1:
                rubros.update({string.split(campo, '-')[1]: valor})
        return rubros
    """ Cómo se va a mostrar el widget
    Retorna la lista de los estudiantes con el campo de nota
    """
    def render(self, name, value, attrs=None, choices=()):
        from django.utils.safestring import mark_safe
        from itertools import chain
        if value is None: value = ''
        output = ['<div class="span12">']
        output.append('<table id="sample-table-1" class="table table-striped table-bordered table-hover">')
        output.append('<thead><tr><th>NRO</th> <th>Rubro</th> <th>Monto</th></tr></thead>')
        num = 0
        output.append('<tbody>')
        for codigo, rubro in chain(self.choices, choices):
            num = num + 1
            output.append('<tr><th>%s</th><td><label >%s</label><input type="hidden" value="codigo-%s"  name=""/></td><td><input type="text" name="rubro-%s" size="3" /></td></tr>' % (num, rubro, codigo, codigo))

        output.append('<tbody>')
        output.append('</table>')
        output.append('</div>')
        return mark_safe('\n'.join(output))

class RubrosField(ModelChoiceField):
    widget=RubrosWidget

    def save_form_data(self, instance, data):
        pass
    """ Validar la data introducida """
    def clean(self,values,initial=None):
        return  values



class RubrosForm(forms.Form):  # [1]
    #rubros = forms.ModelChoiceField(queryset=None, label="Rubros", required=True, empty_label=None)
    rubros = RubrosField(queryset=None, label="Rubros", required=True, empty_label=None)
    #rubros.widget = RubrosWidget()
    def clean_rubros(self):
        subtotales={}
        for (rubroid,monto) in self.cleaned_data.get('rubros').iteritems():
            rubro=Rubro.objects.get(id=rubroid)
            montout=float(rubro.ut)*107
            montoali=float(monto)*rubro.alicuota
            if montout>montoali:
                subtotales[rubroid]=montout

            else:
                subtotales[rubroid]=montoali
        return subtotales


"""Widget Trimestres"""
class TrimestresWidget(forms.widgets.Select):
    attrs = {}

    def __init__(self, attrs=None, choices=()):
        super(TrimestresWidget, self).__init__(attrs)
    """ Retorna la data introducida en forma de diccionario"""
    def value_from_datadict(self, data, files, name):
        import string
        impuestos= {}
        for campo, valor in data.iteritems():
            if campo.find('descuento-') > -1 or campo.find('trimestres-') > -1:
                impuesto=string.split(campo, '-')
                #impuestos.update({data[1]:{[data[0]]:valor}})
                if not impuesto[1] in impuestos.keys():
                    impuestos[impuesto[1]]={}
                impuestos[impuesto[1]].update({impuesto[0]:valor})
        return impuestos
    """ Cómo se va a mostrar el widget
    Retorna la lista de los estudiantes con el campo de nota
    """
    def render(self, name, value, attrs=None, choices=()):
        from django.utils.safestring import mark_safe
        from itertools import chain
        import locale
        locale.setlocale( locale.LC_ALL, '' )
        if value is None: value = ''
        output = ['<div class="span12">']
        output.append('<table id="sample-table-1" class="table table-striped table-bordered table-hover">')
        output.append('<thead><tr><th>C&oacute;digo</th><th>Impuesto</th>  <th>Monto</th><th>Recargo</th> <th>Intereses</th> <th>Subtotal</th><th>Trimestres</th><th>% Descuento</th></tr></thead>')
        num = 0
        output.append('<tbody>')
        if not self.choices[0] is  None:
            for  impuesto in self.choices:
                num = num + 1
                output.append('<tr><td>%(codigo)s</td><td>%(descripcion)s</td><td>%(monto)s</td><td>0</td><td>0</td><td>%(monto)s</td><td><div class="controls"><select name="trimestres-%(codigo)s">"'% ({'codigo':impuesto['impuesto'].codigo,'descripcion':impuesto['impuesto'].descripcion,'monto':locale.currency(impuesto['montos'],grouping=True)} ))
                for trim in range(4,0,-1):
                    output.append('<option value="%(trimestre)s">%(trimestre)s</option>'%({'trimestre':trim}))

            
                output.append('</select></div></td><td><div class="controls"><input name="descuento-%(impuesto)s" type="text" value="0"/></div></tr>'%({'impuesto':impuesto['impuesto'].codigo} ))

            output.append('<tbody>')
            output.append('</table>')
            output.append('</div>')
        return mark_safe('\n'.join(output))

class TrimestresField(ModelChoiceField):
    widget=TrimestresWidget

    #def save_form_data(self, instance, data):
    #    pass
    """ Validar la data introducida """
    def clean(self,values,initial=None):
        return  values


class LiquidacionForm(forms.Form):  # [2]
    trimestre = TrimestresField(queryset=None,required=True)
    numero = forms.CharField(label="Nro. Deposito/Cheque")
    observaciones = forms.CharField(widget=forms.Textarea)
