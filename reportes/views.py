#!-*- coding:  utf-8 -*-
from django.shortcuts import render
import datetime
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer, Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import cm
from reportlab.lib import colors

from liquidaciones.models import Liquidacion


PAGE_HEIGHT = 29.7*cm
PAGE_WIDTH = 21*cm


@login_required(login_url='/login/')
def licencia_expendio_alcohol(request):
    nombre_reporte = "licencia_expendio_alcohol"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nombre_reporte+'.pdf; pagesize=letter;'

    elementos = canvas.Canvas(response)

    elementos.setFont("Helvetica", 11) # Tamaño de letra

    # Primera fila
    elementos.drawCentredString(PAGE_WIDTH-13.5*cm, PAGE_HEIGHT-5.6*cm, 'RODRIGO LEONIDAS BRAVO QUIÑONES')
    elementos.drawCentredString(PAGE_WIDTH-2.5*cm, PAGE_HEIGHT-5.6*cm, '0034530629')

    # Segunda fila
    elementos.drawCentredString(PAGE_WIDTH-18.5*cm, PAGE_HEIGHT-7.3*cm, 'J-19724458-1')
    elementos.drawCentredString(PAGE_WIDTH-13*cm, PAGE_HEIGHT-7.3*cm, 'CERVECERIA POLAR C.A')
    elementos.drawCentredString(PAGE_WIDTH-6.5*cm, PAGE_HEIGHT-7.3*cm, 'V-19724458')
    elementos.drawCentredString(PAGE_WIDTH-2.5*cm, PAGE_HEIGHT-7.3*cm, '0000458585')

    # Tercera fila
    elementos.drawCentredString(PAGE_WIDTH-14.5*cm, PAGE_HEIGHT-9.2*cm, 'Av. Fuerzas Armadas. Calle Zulia # 20')
    elementos.drawCentredString(PAGE_WIDTH-6.2*cm, PAGE_HEIGHT-9.2*cm, 'EZQ. ZAMORA')
    elementos.drawCentredString(PAGE_WIDTH-2.5*cm, PAGE_HEIGHT-9.2*cm, 'COJEDES')

    # Cuarta fila
    elementos.drawCentredString(PAGE_WIDTH-19.2*cm, PAGE_HEIGHT-12.0*cm, '17-04-2009')
    elementos.drawCentredString(PAGE_WIDTH-15.5*cm, PAGE_HEIGHT-12.0*cm, 'CARONÍ')
    elementos.drawCentredString(PAGE_WIDTH-12.3*cm, PAGE_HEIGHT-12.0*cm, 'SAN CARLOS')
    elementos.drawCentredString(PAGE_WIDTH-9.5*cm, PAGE_HEIGHT-12.0*cm, '204515')
    elementos.drawCentredString(PAGE_WIDTH-6.3*cm, PAGE_HEIGHT-12.0*cm, '200.000')
    elementos.drawCentredString(PAGE_WIDTH-2.5*cm, PAGE_HEIGHT-12.0*cm, '9000300001')

    # Quinta fila
    elementos.drawCentredString(PAGE_WIDTH-15.5*cm, PAGE_HEIGHT-14.7*cm, 'Av. Fuerzas Armadas. Calle Zulia # 20')
    elementos.drawCentredString(PAGE_WIDTH-6.5*cm, PAGE_HEIGHT-14.7*cm, '12:30pm')
    elementos.drawCentredString(PAGE_WIDTH-2.5*cm, PAGE_HEIGHT-14.7*cm, '09:00pm')

    # Primera fila último cuadro
    elementos.drawCentredString(PAGE_WIDTH-14.5*cm, PAGE_HEIGHT-24.0*cm, 'RODRIGO BRAVO')
    elementos.drawCentredString(PAGE_WIDTH-4.5*cm, PAGE_HEIGHT-24.0*cm, '09090912')

    # Segunda fila último cuadro
    elementos.drawCentredString(PAGE_WIDTH-16.5*cm, PAGE_HEIGHT-25.5*cm, 'Av. Fuerzas Armadas. Calle Zulia # 20')
    elementos.drawCentredString(PAGE_WIDTH-4.8*cm, PAGE_HEIGHT-24.7*cm, 'J-197244582-2')

    # Tercera fila último cuadro
    elementos.drawCentredString(PAGE_WIDTH-17.5*cm, PAGE_HEIGHT-26.8*cm, 'Luis Alfredo Rodriguez Almeida')
    elementos.drawCentredString(PAGE_WIDTH-11.5*cm, PAGE_HEIGHT-26.7*cm, 'V-19724452')
    elementos.drawCentredString(PAGE_WIDTH-4.5*cm, PAGE_HEIGHT-26.7*cm, '04040452')

    # Cuarta fila último cuadro
    elementos.drawCentredString(PAGE_WIDTH-17.5*cm, PAGE_HEIGHT-27.7*cm, 'Gonzalo Gonzales')
    elementos.drawCentredString(PAGE_WIDTH-11.5*cm, PAGE_HEIGHT-27.7*cm, 'V-19724452')
    elementos.drawCentredString(PAGE_WIDTH-4.5*cm, PAGE_HEIGHT-27.7*cm, '04040452')

    # Quinta fila último cuadro
    elementos.drawCentredString(PAGE_WIDTH-19.2*cm, PAGE_HEIGHT-28.7*cm, '01-02-2014')
    elementos.drawCentredString(PAGE_WIDTH-15.7*cm, PAGE_HEIGHT-28.7*cm, '12:00')
    elementos.drawCentredString(PAGE_WIDTH-4.5*cm, PAGE_HEIGHT-28.7*cm, '04-12-2014')

    elementos.showPage()
    elementos.save()
    return response


@login_required(login_url='/login/')
def vauche_imprimir(request):
    nombre_reporte = "Vauche de Pago"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nombre_reporte+'.pdf; pagesize=letter;'

    elementos = canvas.Canvas(response)

    elementos.setFont("Helvetica", 8) # Tamaño de letra

    elementos.drawCentredString(PAGE_WIDTH-8.5*cm, PAGE_HEIGHT-0.7*cm, 'x')

    # Datos del depositante
    elementos.drawCentredString(PAGE_WIDTH-15.5*cm, PAGE_HEIGHT-2.0*cm, 'Alcaldía de San Carlos')
    elementos.drawCentredString(PAGE_WIDTH-15.5*cm, PAGE_HEIGHT-3.3*cm, 'Luis Carlos Rodriguez Quiñones')
    elementos.drawCentredString(PAGE_WIDTH-15.5*cm, PAGE_HEIGHT-4.0*cm, '20.522.392')

    # n° de cuenta
    elementos.setFont("Helvetica", 12) # Tamaño de letra
    elementos.drawCentredString(PAGE_WIDTH-7.7*cm, PAGE_HEIGHT-1.8*cm, '0  0  0  1  2  3  4  5  6  7  8  9  1  2  3  4  5  6  7  8')

    elementos.showPage()
    elementos.save()
    return response


@login_required(login_url='/login/')
def liquidacion_report(request):
    nombre_reporte = "liquidacion"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nombre_reporte+'.pdf; pagesize=letter;'

    fechas = datetime.datetime.today()
    #Esta lista contendra todos los elementos que se dibujaran en el pdf
    elementos = []
    doc = SimpleDocTemplate(response, title=nombre_reporte, topMargin=20,
                            bottomMargin=20, rightMargin=15, leftMargin=15)

    #---> Encabezado <---
    styleSheet = getSampleStyleSheet()
    cabecera = styleSheet['Normal']
    cabecera.alignment = TA_CENTER
    cabecera.firstLineIndent = 0
    cabecera.fontSize = 10
    cabecera.fontName = 'Helvetica-Bold'
    cabecera.leftIndent = -200
    cabecera.leading = 10

    logo = Image(settings.STATIC_ROOT+'/reportes/escudo.jpg',
                 width=50, height=60)
    logo.hAlign = 'LEFT'
    elementos.append(logo)

    elementos.append(Spacer(1, -50))
    txtEncabezado = 'República Bolivariana de Venezuela'
    txtEncabezado += '<br />Estado Cojedes'
    txtEncabezado += '<br />Alcaldía del Municipio San Carlos'
    txtEncabezado += '<br />Dirección de Rentas Municipales'
    txtEncabezado += '<br />RIF: G-200003371-1'
    encabezado = Paragraph(txtEncabezado, cabecera)
    elementos.append(encabezado)
    #---> Fin Encabezado <---

    #Liquidacion.objects.get()

    #---> Datos Contribuyente <---
    styleSheet2 = getSampleStyleSheet()
    estilo_contrib = styleSheet2['Normal']
    estilo_contrib.alignment = TA_CENTER
    estilo_contrib.fontSize = 10
    estilo_contrib.fontName = 'Helvetica'
    estilo_contrib.leftIndent = 300
    estilo_contrib.leading = 15
    estilo_contrib.borderWidth = 0.50
    estilo_contrib.borderColor = colors.black
    estilo_contrib.borderPadding = 2

    elementos.append(Spacer(1, -50))
    txtContirb = 'INFORMACION GENERAL DEL CONTRIBUYENTE'
    txtContirb += '<br />\t\tnombre '
    txtContirb += '<br />CI/RIF:  Catastro/Placa:'
    texto_contrib = Paragraph(txtContirb, estilo_contrib)
    elementos.append(texto_contrib)
    #---> Fin Datos Contrib <---

    #---> Tabla <---
    elementos.append(Spacer(1, 20))

    estilo_tabla = styleSheet['BodyText']
    estilo_tabla.alignment = TA_CENTER
    x = [
        ('BACKGROUND', (0, 0), (6, 0), colors.silver),
        ('BOX', (0, 5), (6, 0), 0.70, colors.black),
        ('BOX', (0, 9), (6, 0), 0.70, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('GRID', (0, 0), (-1, -1), 0.80, colors.black),
    ]
    tabla = []

    # Headers de la tabla
    hdatos = Paragraph('<b>Fecha Emisión</b>', estilo_tabla)
    x.append(('SPAN', (0, 0), (1, 0))),  # Extendiendo columna
    x.append(('SPAN', (0, 1), (1, 1))),  # Extendiendo columna

    hdatos1 = Paragraph('<b>Fecha Vencimiento</b>', estilo_tabla)
    hdatos2 = Paragraph('<b>ID</b>', estilo_tabla)
    hdatos3 = Paragraph('<b>No. Liquidación</b>', estilo_tabla)

    hdatos4 = Paragraph('<b>No. Deposito</b>', estilo_tabla)
    x.append(('SPAN', (5, 0), (6, 0))),  # Extendiendo columna
    x.append(('SPAN', (5, 1), (6, 1))),  # Extendiendo columna

    hPagos = Paragraph('<b>DETALLE DE PAGO DE IMPUESTOS VARIOS</b>', estilo_tabla)
    x.append(('SPAN', (0, 2), (6, 2))),  # Extendiendo columna

    hpago= Paragraph('<b>Año</b>', estilo_tabla)
    hpago1 = Paragraph('<b>Codigo</b>', estilo_tabla)
    hpago2 = Paragraph('<b>Impuesto</b>', estilo_tabla)
    hpago3 = Paragraph('<b>Monto Impuesto o Tasa</b>', estilo_tabla)
    hpago4 = Paragraph('<b>Recargo</b>', estilo_tabla)
    hpago5 = Paragraph('<b>Intereses</b>', estilo_tabla)
    hpago6 = Paragraph('<b>Sub-Total</b>', estilo_tabla)
    # Fin Headers de la tabla

    tabla.append([hdatos, '', hdatos1, hdatos2, hdatos3, hdatos4, ''])
    tabla.append(['', '', '', '', '', '', ''])

    tabla.append([hPagos])
    tabla.append([hpago, hpago1, hpago2, hpago3, hpago4, hpago5, hpago6])
    tabla.append(['', '', '', '', '', '', ''])

    t = Table(tabla, colWidths=(2.0*cm, 2.0*cm, 3.5*cm, 3.5*cm, 3.5*cm, 2.0*cm, 2.2*cm))
    t.setStyle(TableStyle(x))
    elementos.append(t)
    #---> Fin Tabla <---

    #---> Notas <---
    elementos.append(Spacer(1, 10))
    styleSheet3 = getSampleStyleSheet()
    parrafo = styleSheet3['Normal']
    parrafo.fontsize = 12
    parrafo.rightIndent = -200
    parrafo.fontName = 'Helvetica'
    parrafo.alignment = TA_CENTER
    parrafo.spaceBefore = 15

    txtNota1 = Paragraph('Evite Sanciones...Cumpla con su Ciudad...!', parrafo)
    elementos.append(txtNota1)

    txtNota2 = Paragraph('Para más información dirijase a las oficinas de Rentas Municipales.', parrafo)
    elementos.append(txtNota2)

    txtNota3 = Paragraph('Atención: ING. Glendys Quiñones'+
                         '<br /><b>Directora</b>'+
                         '<br />CONTRIBUYENTE', parrafo)
    elementos.append(txtNota3)
    #---> Fin Notas <---

    #---> Firmas <---
    elementos.append(Spacer(1, -70))
    estilo_tabla2 = styleSheet['BodyText']
    estilo_tabla2.alignment = TA_CENTER
    estilo_tabla2.fontsize = 8
    y = [
        ('BOX', (0, 0), (-1, -1), 0.50, colors.black),
        ('FONT', (0, 0), (-1, -1), "Helvetica", 8),
    ]
    hrecibi = Paragraph('<b>VALIDACIÓN</b>', estilo_tabla2)
    hsellos = Paragraph('<b>SELLOS</b>', estilo_tabla2)
    hautorizada = Paragraph('<b>FIRMA FUNCIONARIO</b>', estilo_tabla2)

    tabla2 = []
    tabla2.append([hrecibi, '\n', '\n'])
    tabla2.append(['\n\n', hsellos, hautorizada])

    t2 = Table(tabla2, colWidths=(3.0*cm, 3.0*cm, 4.0*cm))
    t2.setStyle(TableStyle(y))
    t2.hAlign = 'LEFT'
    elementos.append(t2)
    #---> Fin Firmas <---

    doc.build(elementos)
    return response
