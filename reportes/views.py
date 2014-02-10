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

from liquidaciones.models import Liquidacion2, Pago2


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
def liquidacion_report(request, liquidacion):
    liquid = Liquidacion2.objects.get(numero=liquidacion)
    pagos = Pago2.objects.filter(liquidacion=liquid.pk)

    nombre_reporte = "liquidacion"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nombre_reporte+'.pdf; pagesize=letter;'

    #Esta lista contendra todos los elementos que se dibujaran en el pdf
    elementos = []
    doc = SimpleDocTemplate(response, title=nombre_reporte, topMargin=5,
                            bottomMargin=5, rightMargin=15, leftMargin=15)

    for i in range(0, 3):
        #---> Encabezado <---
        styleSheet = getSampleStyleSheet()
        cabecera = styleSheet['Normal']
        cabecera.alignment = TA_CENTER
        cabecera.firstLineIndent = 0
        cabecera.fontSize = 6
        cabecera.fontName = 'Helvetica-Bold'
        cabecera.leftIndent = -380
        cabecera.leading = 7

        logo = Image(settings.STATIC_ROOT+'/reportes/escudo.jpg',
                    width=25, height=35)
        logo.hAlign = 'LEFT'
        elementos.append(logo)

        elementos.append(Spacer(1, -35))
        txtEncabezado = 'República Bolivariana de Venezuela'
        txtEncabezado += '<br />Estado Cojedes'
        txtEncabezado += '<br />Alcaldía del Municipio San Carlos'
        txtEncabezado += '<br />Dirección de Rentas Municipales'
        txtEncabezado += '<br />RIF: G-200003371-1'
        encabezado = Paragraph(txtEncabezado, cabecera)
        elementos.append(encabezado)
        #---> Fin Encabezado <---

        #---> Datos Contribuyente <---
        styleSheet2 = getSampleStyleSheet()
        estilo_contrib = styleSheet2['BodyText']
        estilo_contrib.alignment = TA_CENTER
        estilo_contrib.fontSize = 7
        estilo_contrib.fontName = 'Times-Roman'
        estilo_contrib.leading = 6
        contrib_style = [
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ]

        elementos.append(Spacer(1, -37))

        contrib1 = Paragraph('<b>INFORMACION GENERAL DEL CONTRIBUYENTE</b>', estilo_contrib)
        contrib2 = Paragraph('%s' % liquid.contribuyente.nombre, estilo_contrib)
        contrib3 = Paragraph('<b>CI/RIF:</b> %s ' % (liquid.contribuyente.num_identificacion), estilo_contrib)

        tabla_contrib = []
        tabla_contrib.append([contrib1])
        tabla_contrib.append([contrib2])
        tabla_contrib.append([contrib3])

        tabla_contrib = Table(tabla_contrib, colWidths=(12.0*cm))
        tabla_contrib.setStyle(TableStyle(contrib_style))
        tabla_contrib.hAlign = 'RIGHT'

        elementos.append(tabla_contrib)
        #---> Fin Datos Contrib <---

        #---> Tabla <---
        elementos.append(Spacer(1, 10))

        estilo_tabla = styleSheet['BodyText']
        estilo_tabla.alignment = TA_CENTER
        estilo_tabla.fontSize = 6
        estilo_tabla.leading = 7
        x = [
            ('BACKGROUND', (0, 0), (6, 0), colors.silver),
            ('BACKGROUND', (0, 2), (6, 2), colors.silver),
            ('BACKGROUND', (0, -2), (-1, -2), colors.silver),
            ('SPAN', (0, -2), (-6, -2)),
            ('SPAN', (0, -1), (-6, -1)),
            ('BOX', (0, 5), (6, 0), 0.50, colors.black),
            ('BOX', (0, 9), (6, 0), 0.50, colors.black),
            ('GRID', (0, 0), (-1, -1), 0.50, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 5.5),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
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

        hpago7 = Paragraph('<b>Credito Fiscal</b>', estilo_tabla)
        hpago8 = Paragraph('<b>Descuento</b>', estilo_tabla)
        hpago9 = Paragraph('<b>Total(Bs.)</b>', estilo_tabla)
        hpago10 = Paragraph('<b>Impuesto o Tasa</b>', estilo_tabla)
        # Fin Headers de la tabla

        tabla.append([hdatos, '', hdatos1, hdatos2, hdatos3, hdatos4, ''])
        tabla.append([liquid.emision, '', liquid.vencimiento, liquid.pk, liquid.numero, liquid.deposito, ''])
        pos = 0
        recargo = 0
        intereses = 0
        cancelado = 0
        monto = 0
        for pago in pagos:

            if pos == 0:
                tabla.append([hPagos])
                tabla.append([hpago, hpago1, hpago2, hpago3, hpago4, hpago5, hpago6])
            tabla.append([liquid.ano, pago.impuesto.codigo, pago.impuesto.descripcion, pago.monto, pago.recargo, pago.intereses, pago.cancelado])

            pos = pos + 1

            recargo = recargo + pago.recargo
            intereses = intereses + pago.intereses
            cancelado = cancelado + pago.cancelado
            monto = monto + pago.monto

        tabla.append([hpago7, '', hpago8, hpago10, hpago4, hpago5, hpago9])
        tabla.append(['0', '', pago.descuento, cancelado, recargo, intereses, monto])

        t = Table(tabla, colWidths=(2.0*cm, 2.0*cm, 3.5*cm, 3.5*cm, 3.5*cm, 2.0*cm, 2.2*cm))
        t.setStyle(TableStyle(x))
        elementos.append(t)
        #---> Fin Tabla <---

        #---> Notas <---
        styleSheetNota = getSampleStyleSheet()
        nota = styleSheetNota['Normal']
        nota.fontSize = 6
        nota.fontName = 'Helvetica'
        nota.alignment = TA_LEFT

        txtNota1 = Paragraph('<b>DETALLES:</b> <br /> <b>%s</b>' % liquid.observaciones, nota)
        elementos.append(txtNota1)

        elementos.append(Spacer(1, 10))
        styleSheet3 = getSampleStyleSheet()
        parrafo = styleSheet3['Normal']
        parrafo.fontSize = 6
        parrafo.rightIndent = -320
        parrafo.fontName = 'Helvetica'
        parrafo.alignment = TA_CENTER

        elementos.append(Spacer(1, -17))
        txtNota1 = Paragraph('Evite Sanciones...Cumpla con su Ciudad...!', parrafo)
        elementos.append(txtNota1)

        txtNota2 = Paragraph('Para más información dirijase a las oficinas de Rentas Municipales.'+
                             '<br />Atención: ING. Glendys Quiñones' +
                             '<br /><b>Directora</b>', parrafo)
        elementos.append(txtNota2)
        #---> Fin Notas <---

        #---> Firmas <---
        elementos.append(Spacer(1, -42))
        estilo_tabla2 = styleSheet['BodyText']
        estilo_tabla2.alignment = TA_CENTER
        estilo_tabla2.fontSize = 5
        y = [
            ('BOX', (0, 0), (-1, -1), 0.50, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ]
        hrecibi = Paragraph('VALIDACIÓN', estilo_tabla2)
        hsellos = Paragraph('SELLOS', estilo_tabla2)
        hautorizada = Paragraph('FIRMA FUNCIONARIO', estilo_tabla2)

        tabla2 = []
        tabla2.append([hrecibi, '', ''])
        tabla2.append(['', hsellos, hautorizada])

        t2 = Table(tabla2, colWidths=(3.0*cm, 3.0*cm, 4.0*cm))
        t2.setStyle(TableStyle(y))
        t2.hAlign = 'LEFT'
        elementos.append(t2)
        #---> Fin Firmas <---

        elementos.append(Spacer(1, 5))
        lineaStyle = [
            ('LINEABOVE', (0, 0), (-1, -1), 0.35, colors.black),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 2),
        ]
        linea = []
        linea.append([' '])

        l2 = Table(linea, colWidths=(20.0*cm))
        l2.setStyle(TableStyle(lineaStyle))
        elementos.append(l2)

    doc.build(elementos)
    return response
