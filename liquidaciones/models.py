from django.db import models
from django.contrib.auth.models import User


class Impuesto(models.Model):
    codigo=models.IntegerField()
    descripcion=models.CharField(max_length=200,default='Sin definir')

    def __unicode__(self):
        return '%s - %s'%(self.codigo,self.descripcion)


class Liquidacion(models.Model):
    numero=models.CharField(max_length=20)
    trimestre=models.IntegerField()
    ano=models.IntegerField()
    monto=models.FloatField()
    recargo=models.FloatField()
    intereses=models.FloatField()
    impuesto=models.ForeignKey(Impuesto)
    emision=models.DateField()
    liquidador=models.ForeignKey(User)

    def __unicode__(self):
        return '%s - %s' % (self.numero, self.monto)


class Pago(models.Model):
    from contribuyentes.models import Contribuyente

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
    fecha_pago=models.DateField()
    observaciones=models.TextField(null=True)
