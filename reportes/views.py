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
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors


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
