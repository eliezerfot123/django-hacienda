from django.db import models
from liquidaciones.models import Liquidacion 

# Create your models here.
class Rubro(models.Model):
    codigo=models.IntegerField()
    rubro=models.CharField(max_length=500)
    alicuota=models.FloatField()
    ut=models.IntegerField()
    def __unicode__(self):
        return '%d %s (%d UT)'%(self.codigo,self.rubro,self.ut)

class Licencia(models.Model):
    serial=models.CharField(max_length=20)
    control=models.CharField(max_length=20)
    numero=models.CharField(max_length=20)
    cantidad=models.IntegerField(null=True,blank=True)
    emision=models.DateField()
    valido=models.DateField()
    campoid=models.IntegerField(null=True,blank=True)

class Contribuyente(models.Model):
    id_contrato=models.IntegerField()
    num_identificacion=models.CharField(max_length=50)
    nombre=models.CharField(max_length=200)
    telf=models.CharField(null=True,blank=True,max_length=100)
    fax=models.CharField(null=True,blank=True,max_length=100)
    email=models.CharField(null=True,blank=True,max_length=50)
    representante=models.CharField(null=True,blank=True,max_length=200)
    cedula_rep=models.CharField(null=True,max_length=30)
    capital=models.FloatField()
    direccion=models.CharField(null=True,blank=True,max_length=300)
    rubro=models.ManyToManyField(Rubro,null=True)
    modificado=models.DateField()

    def __unicode__(self):
        return '%s %s %s'%(self.num_identificacion,self.nombre,self.representante)


    def licencias(self,):
        return Licencia.object.filter(contribuyente=self.pk)

    def liquidaciones(self):
        return Liquidacion.objects.filter(contribuyente=self.pk)





