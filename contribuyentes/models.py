from django.db import models

# Create your models here.
class Rubro(models.Model):
    codigo=models.IntegerField()
    rubro=models.CharField(max_length=500)
    alicuota=models.FloatField()
    ut=models.IntegerField()
    def __unicode__(self):
        return '%d %s (%d UT)'%(self.codigo,self.rubro,self.ut)


class Contribuyente(models.Model):
    id_contrato=models.IntegerField(unique=True,null=True)
    num_identificacion=models.CharField(max_length=50)
    nombre=models.CharField(max_length=200)
    telf=models.CharField(null=True,blank=True,max_length=100)
    fax=models.CharField(null=True,blank=True,max_length=100)
    email=models.CharField(null=True,blank=True,max_length=50)
    representante=models.CharField(null=True,blank=True,max_length=200)
    cedula_rep=models.CharField(null=True,blank=True,max_length=30)
    capital=models.FloatField(default=0.0)
    direccion=models.CharField(null=True,blank=True,max_length=300)
    rubro=models.ManyToManyField(Rubro,null=True,blank=True)
    modificado=models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '%d %s %s %s'%(self.id_contrato,self.num_identificacion,self.nombre,self.representante)
    
    def save(self):
        if not self.id_contrato:
            from django.db.models import Max
            self.id_contrato=Contribuyente.objects.all().aggregate(Max('id_contrato'))['id_contrato__max']+1
        return super(Contribuyente,self).save(self)
            

    def licencias(self,):
        return Licencia.object.filter(contribuyente=self.pk)

    def liquidaciones(self,contrib):
        from liquidaciones.models import Pago
        return Pago.objects.filter(contribuyente=self)

class Licencia(models.Model):
    serial=models.CharField(max_length=20)
    control=models.CharField(max_length=20)
    numero=models.CharField(max_length=20)
    cantidad=models.IntegerField(null=True,blank=True)
    emision=models.DateField()
    valido=models.DateField()
    #campoid=models.IntegerField(null=True,blank=True)
    contribuyente=models.ForeignKey(Contribuyente)
