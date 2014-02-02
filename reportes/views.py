from django.shortcuts import render
import datetime
from django.conf import settings
from django.http import HttpResponse

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer, Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors


def licencia_expendio_alcohol(request):
    nombre_reporte = "licencia_expendio_alcohol"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nombre_reporte+'.pdf; pagesize=letter;'

    fechas = datetime.datetime.today()
    #Esta lista contendra todos los elementos que se dibujaran en el pdf
    elementos = []
    doc = SimpleDocTemplate(response, title=nombre_reporte, topMargin=5, bottomMargin=5, rightMargin=5, leftMargin=5)

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
    encabezado = Paragraph(txtEncabezado, cabecera)
    elementos.append(encabezado)
    #---> Fin Encabezado <---

    #---> Fechas <---
    styleSheet2 = getSampleStyleSheet()
    estilo_fechas = styleSheet2['Normal']
    estilo_fechas.alignment = TA_RIGHT
    estilo_fechas.fontSize = 10
    estilo_fechas.fontName = 'Helvetica'
    estilo_fechas.rightIndent = 130
    estilo_fechas.leading = 15

    elementos.append(Spacer(1, -40))
    txtFechas = 'Fecha de Solicitud: '
    txtFechas += '<br />Valido Hasta: '
    txtFechas += '<br />N° de Solicitud: '
    txtFechas += '<br />N° de Autorización: '
    texto_fechas = Paragraph(txtFechas, estilo_fechas)
    elementos.append(texto_fechas)
    #---> Fin Fechas <---

    #---> Titulo <---
    estilo_titulo = styleSheet['Heading1']
    estilo_titulo.alignment = TA_CENTER
    estilo_titulo.fontSize = 18
    estilo_titulo.fontName = 'Helvetica-Bold'

    txtTitulo = 'AUTORIZACION PARA EL EXPENDIO DE ALCOHOL Y ESPECIES ALCOHOLICAS'
    texto_titulo = Paragraph(txtTitulo, estilo_titulo)
    elementos.append(texto_titulo)
    #---> Fin Titulo <---

    #---> Tabla <---
    estilo_tabla = styleSheet['BodyText']
    estilo_tabla.alignment = TA_LEFT
    x = [
        ('BOX', (0, 6), (3, 0), 0.70, colors.black),
        ('BOX', (0, 5), (3, 0), 0.70, colors.black),
        ('BOX', (0, 9), (3, 0), 0.70, colors.black),
        ('INNERGRID', (0, 1), (-1, 4), 0.35, colors.black),
        ('INNERGRID', (0, 6), (-1, 8), 0.35, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        #('GRID', (0, 0), (-1, -1), 0.80, colors.black),
    ]
    tabla = []

    # Headers de la tabla
    hdatos = Paragraph('<b>DATOS PERSONALES</b>', estilo_tabla)
    hdatosBancario = Paragraph('<b>DATOS BANCARIOS</b>', estilo_tabla)

    nombre = Paragraph('NOMBRE O RAZÓN SOCIAL:<br /><br /> ', estilo_tabla)
    licencia = Paragraph('N° DE LICENCIA:<br /><br /> ', estilo_tabla)
    rif = Paragraph('R.I.F.:<br /><br /> ', estilo_tabla)
    representante = Paragraph('REPRESENTANTE LEGAL:<br /><br /> ', estilo_tabla)
    cedula = Paragraph('C.I.:<br /><br /> ', estilo_tabla)
    ID = Paragraph('ID:<br /><br /> ', estilo_tabla)
    direccion = Paragraph('DIRECCION DEL ESTABLECIMIENTO:<br /><br /> ', estilo_tabla)
    municipio = Paragraph('MUNICIPIO:<br /><br /> ', estilo_tabla)
    estado = Paragraph('ESTADO:<br /><br /> ', estilo_tabla)
    fechaPago = Paragraph('FECHA DE PAGO:<br /><br /> ', estilo_tabla)
    banco = Paragraph('ENTIDAD BANCARIA:<br /><br /> ', estilo_tabla)

    sucursal = Paragraph('SUCURSAL:<br /><br /> ', estilo_tabla)
    x.append(('SPAN', (2, 6), (3, 6))), # Extendiendo columna sucursal

    numero = Paragraph('NÚMERO:<br /><br /> ', estilo_tabla)
    monto = Paragraph('MONTO (Bs.):<br /><br /> ', estilo_tabla)

    liquidacion = Paragraph('LIQUIDACIÓN:<br /><br /> ', estilo_tabla)
    x.append(('SPAN', (2, 7), (3, 7))), # Extendiendo columna liquidacion

    expendio = Paragraph('CLASIFICACIÓN DE EXPENDIO:<br /><br /> ', estilo_tabla)
    horario = Paragraph('HORARIO:<br /><br /> ', estilo_tabla)

    horarioExtendido = Paragraph('HORARIO EXTENDIDO:<br /><br /> ', estilo_tabla)
    x.append(('SPAN', (2, 8), (3, 8))), # Extendiendo columna horarioExtendido

    tabla.append([hdatos])
    tabla.append([nombre, licencia])
    tabla.append([rif, representante, cedula, ID])
    tabla.append([direccion, ''])
    tabla.append([municipio, estado])

    tabla.append([hdatosBancario])
    tabla.append([fechaPago, banco, sucursal])
    tabla.append([numero, monto, liquidacion])
    tabla.append([expendio, horario, horarioExtendido])

    t = Table(tabla, colWidths=(7.0*cm, 6.4*cm, 3.0*cm, 3.0*cm))
    t.setStyle(TableStyle(x))
    elementos.append(t)
    #---> Fin Tabla <---

    #---> Notas <---
    styleSheet3 = getSampleStyleSheet()
    parrafo = styleSheet3['Normal']
    parrafo.fontsize = 12
    parrafo.leftIndent = 15
    parrafo.rightIndent = 15
    parrafo.fontName = 'Helvetica'
    parrafo.alignment = TA_LEFT
    parrafo.spaceBefore = 15
    parrafo.borderWidth = 0.35
    parrafo.borderColor = colors.black
    parrafo.borderPadding = 5

    txtNota1 = Paragraph('Se expide la presente constancia como prueba de '+
                         'haber cancelado, la tasa de RENOVACION, prevista '+
                         'en los Ordinales N° 1 y 2 del Art. 10 de la Ley de '+
                         'Timbres Fiscales Vigentes.', parrafo)
    elementos.append(txtNota1)

    txtNota2 = Paragraph('NOTA: De conformidad con lo establecido en el Articulo 10 ' +
                         'de la Ley de Timbres Fiscales, los contribuyentes deben ' +
                         'renovar sus Autorizaciones de Expendios de Bebidas Alcohólicas ' +
                         'anualmente, antes de la fecha en que fue entregado, así ' +
                         'como cumplir con todos los tramites que modifiquen el ' +
                         'registro conforme a la Ley de Impuesto sobre Alcoholes ' +
                         'y Especies Alcohólicas y su reglamento. En caso contrario ' +
                         'serán sancionados de acuerdo a lo establecido en el ' +
                         'Artículo 108 del Código Orgánico Tributario vigente.' +
                         '<br />APEGARSE A DAR CUMPLIMIENTO A LO CONTEMPLADO ' +
                         'EN EL DECRETO No. 001-06 DE FECHA 04-01-2006 EMITIDO ' +
                         'POR LA MAXIMA AUTORIDAD DEL MUNICIPIO AUTONOMO SAN CARLOS ' +
                         ', DONDE SE REGULA LA VENTA DE BEBIDAS ALCOHOLICAS, ' +
                         'ASI COMO TAMBIEN LA REGULACION DE LOS HORARIOS ' +
                         'PERMITIDOS PARA EXPENDER LICORES.', parrafo)
    elementos.append(txtNota2)
    #---> Fin Notas <---

    #---> Firmas <---
    elementos.append(Spacer(1, 10))
    y = [
        ('GRID', (0, 0), (-1, -1), 0.50, colors.black),
    ]
    hrecibi = Paragraph('<b>RECIBI CONFORME</b>', estilo_tabla)
    hsellos = Paragraph('<b>SELLOS</b>', estilo_tabla)
    hautorizada = Paragraph('<b>FIRMA AUTORIZADA</b>', estilo_tabla)

    estilo_tabla.fontSize = 8
    datosRecibi = Paragraph('Nombre: <br /><br />C.I.:' +
                            '<br /><br />Firma:<br /><br />', estilo_tabla)

    tabla2 = []
    tabla2.append([hrecibi, hsellos, hautorizada])
    tabla2.append([datosRecibi, '', ''])

    t2 = Table(tabla2, colWidths=(6.0*cm, 6.0*cm, 6.0*cm))
    t2.setStyle(TableStyle(y))
    elementos.append(t2)
    #---> Fin Firmas <---

    #---> Tabla3 autorizacion <---
    elementos.append(Spacer(1, 10))
    estilo_tabla3 = styleSheet['BodyText']
    estilo_tabla3.alignment = TA_LEFT
    z = [
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('GRID', (0, 0), (-1, -1), 0.80, colors.black),
        ('FONT', (0, 0), (3, 0), "Helvetica-Bold", 12),
        ('FONT', (0, 0), (-1, -1), "Helvetica", 8),
        ('SPAN', (0, 0), (3, 0)),
        ('ALIGN', (0, 0), (3, 0), 'CENTER'),
    ]
    tabla3 = []

    # Headers de la tabla3
    aNombre = Paragraph('NOMBRE O RAZÓN SOCIAL:<br /><br /> ', estilo_tabla3)
    z.append(('SPAN', (0, 1), (1, 1))),

    aAutorizacion = Paragraph('N° DE AUTORIZACION:<br /><br /> ', estilo_tabla3)
    z.append(('SPAN', (2, 1), (3, 1))),

    aLicencia = Paragraph('N° DE LICENCIA:<br /><br /> ', estilo_tabla3)

    aRif = Paragraph('R.I.F.', estilo_tabla3)
    z.append(('SPAN', (2, 2), (3, 2))),

    aDireccion = Paragraph('DIRECCION DEL ESTABLECIMIENTO:' +
                           '<br /><br /><br /><br />', estilo_tabla3)
    # (col,fila, col,fila)
    z.append(('SPAN', (1, 3), (0, 2))),
    z.append(('VALIGN', (1, 2), (0, 2), 'TOP')),

    tabla3.append(['AUTORIZACION PARA EL EXPENDIO DE ALCOHOL ' +
                    'Y ESPECIES ALCOHOLICAS'])
    tabla3.append([aNombre, '', aAutorizacion])
    tabla3.append([aDireccion, '', aRif])
    tabla3.append(['', '', aLicencia])
    tabla3.append(['ENTREGADO POR:\n ', '', 'C.I.\n ', 'ID:\n '])
    z.append(('SPAN', (1, 4), (0, 4))),
    tabla3.append(['RECIBIDO POR:\n ', '', 'C.I.\n ', 'LIQUIDACION:\n '])
    z.append(('SPAN', (1, 5), (0, 5))),
    tabla3.append(['FECHA:\n ', 'HORA:\n ', 'FIRMA:\n ', 'VENCIMIENTO:\n '])

    t3 = Table(tabla3, colWidths=(5.0*cm, 5.0*cm, 4.5*cm, 4.5*cm))
    t3.setStyle(TableStyle(z))
    elementos.append(t3)
    #---> Fin tabla3 autorizacion <---

    doc.build(elementos)

    return response
