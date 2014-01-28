from django.db import models

# Create your models here.

class Impuesto(models.Model):
    codigo=models.IntegerField()
    descripcion=models.CharField(max_length=200,default='Sin definir')


class Liquidacion(models.Model):
    numero=models.CharField(max_length=20)
    trimestre=models.IntegerField()
    ano=models.IntegerField()
    monto=models.FloatField()
    recargo=models.FloatField()
    intereses=models.FloatField()
    impuesto=models.ForeignKey(Impuesto)
    emision=models.DateField()
