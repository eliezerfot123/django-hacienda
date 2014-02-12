# -*- coding: utf8 -*-
from django import forms
from django.db.models import Q

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
            if campo.find('definitiva-') > -1:
                datos=string.split(campo,'-')
                if not datos[1]  in rubros.keys():
                    rubros[datos[1]]={}
                rubros[datos[1]].update({string.split(campo, '-')[2]: valor})
            if campo.find('estimada-')> -1:
                datos=string.split(campo,'-')
                if not datos[1]  in rubros.keys():
                    rubros[datos[1]]={}
                rubros[datos[1]].update({string.split(campo, '-')[2]: valor})

        return rubros
    """ Cómo se va a mostrar el widget
    Retorna la lista de los estudiantes con el campo de nota
    """
    def render(self, name, value, attrs=None, choices=()):
        from django.utils.safestring import mark_safe
        import datetime 
        if value is None: value = ''
        output = ['<div class="span12">']
        output.append('<table id="montos" class="table table-striped table-bordered table-hover">')
        output.append('<thead><tr><th>Año</th> <th style="width: 300px">Rubro</th> <th>Monto Estimado </th><Th>Monto Definitivo</th></tr></thead>')
        output.append('<tbody>')
        for pagos in self.choices.queryset.filter(definitivo=None):
            output.append('<tr><th>%s</th><th><label >%s</label></th></td><td>'%(pagos.ano,pagos.rubro))
            if pagos.estimado is None: 
                output.append('<input type="text" style="width: 100px;" name="estimada-%s-%s" size="3" />'%(pagos.ano, pagos.rubro.codigo))
            else:
                output.append('%s'%(pagos.estimado))
            output.append('</td>')
            if pagos.definitivo is None and pagos.ano < datetime.date.today().year:
                output.append('<td><input type="text"  style="width: 100px;" name="definitiva-%s-%s" size="3" /></td>'%(pagos.ano, pagos.rubro.codigo))
            output.append('</tr>' )

        output.append('<tbody>')
        output.append('</table>')
        output.append('</div>')
        return mark_safe('\n'.join(output))

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
            if campo.find('descuento-') > -1 or campo.find('trimestres-') > -1 or campo.find('intereses-')>-1 or campo.find('cancelado-')>-1or campo.find('monto-') > -1 or campo.find('recargo-')>-1:
                impuesto=string.split(campo, '-')
                #impuestos.update({data[1]:{[data[0]]:valor}})
                if not impuesto[1] in impuestos.keys():
                    impuestos[impuesto[1]]={impuesto[2]:{}}
                impuestos[impuesto[1]][impuesto[2]].update({impuesto[0]:valor})
        return impuestos

    def render(self, name, value, attrs=None, choices=()):
        from django.utils.safestring import mark_safe
        from itertools import chain
        if value is None: value = ''
        output = ['<div class="span12">']
        output.append('<table id="sample-table-1" class="table table-striped table-bordered table-hover">')
        output.append('<thead><tr><th>A&ntilde;o</th><th>C&oacute;digo</th><th>Impuesto</th>  <th>Monto</th><th>Recargo</th> <th>Intereses</th><th>Trimestres</th><th>% Descuento</th> <th>Subtotal</th></tr></thead>')
        num = 0
        output.append('<tbody>')
        if not self.choices[0] is  None:
            for  impuesto in self.choices:
                num = num + 1
                for ano,monto in impuesto['montos'].iteritems():
                    output.append('<tr><td>%(ano)s</td><td>%(codigo)s</td><td>%(descripcion)s</td><td>%(monto)s BsF.<input type="hidden" name="monto-%(codigo)s-%(ano)s" value="%(monto)s"/> </td><td><input type="text" value="0" name="recargo-%(codigo)s-%(ano)s" style="width: 60px" /></td><td><input type="text" style="width: 60px" value="0" name="intereses-%(codigo)s-%(ano)s" /></td><td><div class="controls"><select  style="width: 60px" name="trimestres-%(codigo)s-%(ano)s">'% ({'codigo':impuesto['impuesto'].codigo,'descripcion':impuesto['impuesto'].descripcion,'monto':monto,'ano':ano} ))
                    for trim in range(4,0,-1):
                        output.append('<option value="%(trimestre)s">%(trimestre)s</option>'%({'trimestre':trim}))


                    output.append('</select></div></td><td><div class="controls"><input name="descuento-%(impuesto)s-%(ano)s" type="text"  style="width: 60px" value="0"/></div></td><td><div id="subtotal-%(impuesto)s-%(ano)s">%(monto)s</div> BsF.</td><input type="hidden" name="cancelado-%(impuesto)s-%(ano)s" value="%(monto)s" /> </tr>'%({'impuesto':impuesto['impuesto'].codigo,'monto':monto,'ano':ano} ))

            output.append('</tbody>')
            output.append('</table>')
            output.append('</div>')
        return mark_safe('\n'.join(output))


"""Widget Rubros"""
class EstimadasWidget(forms.widgets.Select):
    attrs = {}

    def __init__(self, attrs=None, choices=()):
        super(EstimadasWidget, self).__init__(attrs)
        self.choices = list(choices)
    """ Retorna la data introducida en forma de diccionario"""
    def value_from_datadict(self, data, files, name):
        import string
        rubros = {}
        for campo, valor in data.iteritems():
            if campo.find('estimada-')> -1:
                datos=string.split(campo,'-')
                if not datos[1]  in rubros.keys():
                    rubros[datos[1]]={}
                rubros[datos[1]].update({string.split(campo, '-')[2]: valor})

        return rubros
    """ Cómo se va a mostrar el widget
    Retorna la lista de los estudiantes con el campo de nota
    """
    def render(self, name, value, attrs=None, choices=()):
        from django.utils.safestring import mark_safe
        import datetime 
        if value is None: value = ''
        output = ['<div class="span12">']
        output.append('<table id="montos" class="table table-striped table-bordered table-hover">')
        output.append('<thead><tr><th>Año</th> <th style="width: 300px">Rubro</th> <th>Monto Estimado </th></tr></thead>')
        output.append('<tbody>')
        for pagos in self.choices.queryset.filter(Q(estimado=None)|Q(ano=datetime.date.today().year)):
            output.append('<tr><th>%s</th><th><label >%s</label></th></td><td>'%(pagos.ano,pagos.rubro))
            if pagos.estimado is None: 
                output.append('<input type="text" style="width: 100px;" name="estimada-%s-%s" size="3" />'%(pagos.ano, pagos.rubro.codigo))
            elif   pagos.ano == datetime.date.today().year:
                output.append('%s <input type="hidden" name="estimada-%s-%s" value="%s" />'%(pagos.estimado,pagos.ano, pagos.rubro.codigo,pagos.estimado))
            output.append('</td>')
            output.append('</tr>' )

        output.append('<tbody>')
        output.append('</table>')
        output.append('</div>')
        return mark_safe('\n'.join(output))
