from django.shortcuts import render
import datetime
from django.conf import settings
from django.http import HttpResponse

from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate, PageTemplate
from reportlab.platypus import Spacer, Paragraph, Table, TableStyle, Frame, Image
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm, mm
from reportlab.lib import colors

PAGE_HEIGHT = 29.7*cm
PAGE_WIDTH = 21*cm

def cabecera_licencias(canvas, doc):
    canvas.saveState()
    #canvas.drawImage(settings.STATIC_ROOT+'reportes/unerg.jpg', 2.6*cm, PAGE_HEIGHT-4.5*cm, width = 100, height = 38)
    canvas.setFont("Helvetica-Bold",9)
    canvas.drawCentredString(PAGE_WIDTH-9.5*cm, PAGE_HEIGHT-3.6*cm, u'República Bolivariana de Venezuela')
    canvas.drawCentredString(PAGE_WIDTH-9.5*cm, PAGE_HEIGHT-4.0*cm, u'Estado Cojedes')
    canvas.drawCentredString(PAGE_WIDTH-9.5*cm, PAGE_HEIGHT-4.4*cm, u'Alcaldía del Municipio Ezequiel Zamora')
    canvas.drawCentredString(PAGE_WIDTH-9.5*cm, PAGE_HEIGHT-4.8*cm, u'Dirección de Rentas Municipales')
    canvas.restoreState()
    canvas.saveState()


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
    txtEncabezado = u'República Bolivariana de Venezuela'
    txtEncabezado += u'<br />Estado Cojedes'
    txtEncabezado += u'<br />Alcaldía del Municipio San Carlos'
    txtEncabezado += u'<br />Dirección de Rentas Municipales'
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
    txtFechas = u'Fecha de Solicitud: '
    txtFechas += u'<br />Valido Hasta: '
    txtFechas += u'<br />N° de Solicitud: '
    txtFechas += u'<br />N° de Autorización: '
    texto_fechas = Paragraph(txtFechas, estilo_fechas)
    elementos.append(texto_fechas)
    #---> Fin Fechas <---

    #---> Titulo <---
    estilo_titulo = styleSheet['Heading1']
    estilo_titulo.alignment = TA_CENTER
    estilo_titulo.fontSize = 18
    estilo_titulo.fontName = 'Helvetica-Bold'

    txtTitulo = u'AUTORIZACION PARA EL EXPENDIO DE ALCOHOL Y ESPECIES ALCOHOLICAS'
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

    nombre = Paragraph('NOMBRE O RAZÓN SOCIAL:<br />.', estilo_tabla)
    licencia = Paragraph('N° DE LICENCIA:<br />.', estilo_tabla)
    rif = Paragraph('R.I.F.:<br />.', estilo_tabla)
    representante = Paragraph('REPRESENTANTE LEGAL:<br />.', estilo_tabla)
    cedula = Paragraph('C.I.:<br />.', estilo_tabla)
    ID = Paragraph('ID:<br />.', estilo_tabla)
    direccion = Paragraph('DIRECCION DEL ESTABLECIMIENTO:<br />.', estilo_tabla)
    municipio = Paragraph('MUNICIPIO:<br />.', estilo_tabla)
    estado = Paragraph('ESTADO:<br />.', estilo_tabla)
    fechaPago = Paragraph('FECHA DE PAGO:<br />.', estilo_tabla)
    banco = Paragraph('ENTIDAD BANCARIA:<br />.', estilo_tabla)
    sucursal = Paragraph('SUCURSAL:<br />.', estilo_tabla)
    numero = Paragraph('NÚMERO:<br />.', estilo_tabla)
    monto = Paragraph('MONTO (Bs.):<br />.', estilo_tabla)
    liquidacion = Paragraph('LIQUIDACIÓN:<br />.', estilo_tabla)
    expendio = Paragraph('CLASIFICACIÓN DE EXPENDIO:<br />.', estilo_tabla)
    horario = Paragraph('HORARIO:<br />.', estilo_tabla)
    horarioExtendido = Paragraph('HORARIO EXTENDIDO:<br />.', estilo_tabla)

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
    elementos.append(Spacer(1, 20))
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

    doc.build(elementos)

    return response
