# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from contribuyentes.models import Contribuyente

class UT(models.Model):
    ano=models.IntegerField()
    valor=models.FloatField()
    def __unicode__(self):
        return '%d %d'%(self.ano,self.valor)


class Impuesto(models.Model):
    codigo=models.IntegerField()
    descripcion=models.CharField(max_length=200,default='Sin definir')

    def __unicode__(self):
        return '%s - %s'%(self.codigo,self.descripcion)

class Cuota(models.Model):
    orden=models.IntegerField()
    tipo=models.CharField(max_length=4,choices=(('SEM','Semana'),('TRIM','Trimestre'),('MENS','Mensualidad'),('ANUA','Año')))
    def __unicode__(self):
        return '%d %s'%(self.orden,self.get_tipo_display())

    class Meta:
        ordering=['tipo','orden']
        
class Liquidacion(models.Model):
    numero=models.CharField(max_length=20)
    trimestre=models.IntegerField()
    ano=models.IntegerField()
    monto=models.FloatField()
    recargo=models.FloatField()
    intereses=models.FloatField()
    impuesto=models.ForeignKey(Impuesto)
    emision=models.DateField()
    liquidador=models.ForeignKey(User,null=True)

    def __unicode__(self):
        return '%s - %s' % (self.numero, self.monto)

    def as_dict(self):
        return {
            "name": "%s %s %s"%( self.numero,self.monto,self.pago_set.all()),
            "pk": self.pk,
        }

class Liquidacion2(models.Model):
    numero=models.CharField(max_length=20)
    ano=models.IntegerField()
    deposito=models.CharField(max_length=20)
    modopago=models.CharField(max_length=2,choices=(('CH','Cheque'),('DP','Deposito'),('TF','Transferencia')),default='DP')
    fecha_pago=models.DateField(null=True)
    emision=models.DateField()
    liquidador=models.ForeignKey(User)
    contribuyente=models.ForeignKey(Contribuyente)
    vencimiento=models.DateField()
    observaciones=models.TextField(max_length=200,blank=True,null=True)

    def save(self):
        if not self.id:
            self.numero='10000%03d%d'%(self.liquidador.id,Liquidacion2.objects.filter(liquidador=self.liquidador).count()+1)
        super(Liquidacion2,self).save()

    def as_dict(self):
        return {
            "name": "%s  Nro.:%s"%( self.numero,self.deposito),
            "pk": self.pk,
        }

    def __unicode__(self):
        return '%s - %s' % (self.numero, self.contribuyente)

class Pago2(models.Model):
    liquidacion=models.ForeignKey(Liquidacion2)
    impuesto=models.ForeignKey(Impuesto)
    ut=models.ForeignKey(UT)
    descuento=models.FloatField(default=0.0)
    trimestres=models.ManyToManyField(Cuota)
    intereses=models.FloatField(default=0.0)
    recargo=models.FloatField(default=0.0)
    monto=models.FloatField() # Sub-Total
    cancelado=models.FloatField() # ToTal
    credito_fiscal=models.FloatField(null=True,default=0.0)
    tipo=models.CharField(max_length=3,choices=(('EST','Estimada'),('DEF','Definitiva'),('SND','Sin Definir')), default='SND')
    def __unicode__(self):
        return '%s'%self.cancelado





class Pago(models.Model):

    liquidacion=models.ForeignKey(Liquidacion,null=True)
    num_liquidacion=models.CharField(null=True,max_length=20)
    contribuyente=models.ForeignKey(Contribuyente)
    deposito=models.CharField(max_length=20)
    emision=models.DateField()
    vencimiento=models.DateField()
    credito_fiscal=models.FloatField(null=True,default=0.0)
    descuento=models.FloatField(null=True,default=0.0)
    impuesto=models.FloatField()
    recargo=models.FloatField(null=True,default=0.0)
    intereses=models.FloatField(null=True,default=0.0)
    fecha_pago=models.DateField(null=True,blank=True)
    observaciones=models.TextField(null=True)
