from django.db import models

# Create your models here.
class Rubros(models.Model):
    codigo=models.IntegerField()
    rubro=models.CharField(max_length=500)
    alicuota=models.FloatField()
    ut=models.IntegerField()
    def __unicode__(self):
        return u'%d %s (%d UT)'%(self.codigo,self.rubro,self.ut)

class Contribuyente(models.Model):
    id_contrato=models.IntegerField()
    num_identificacion=models.CharField(max_length=50)
    nombre=models.CharField(max_length=200)
    telf=models.CharField(null=True,blank=True,max_length=100)
    fax=models.CharField(null=True,blank=True,max_length=100)
    email=models.CharField(null=True,blank=True,max_length=50)
    representante=models.CharField(null=True,blank=True,max_length=200)
    rubro=models.ForeignKey(Rubros)
    def __unicode__(self):
        return u'%s %s %s'%(self.num_identificacion,self.nombre,self.representante)


