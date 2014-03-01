from django.test import TestCase
import factory
from factory import fuzzy
from django.contrib.auth.models import User
class ContribuyenteFactory(factory.DjangoModelFactory):
    FACTORY_FOR='contribuyentes.Contribuyente'
    FACTORY_DJANGO_GET_OR_CREATE=('id_contrato','num_identificacion','nombre',)
    id_contrato=fuzzy.FuzzyInteger(1000,2000)
    num_identificacion=fuzzy.FuzzyInteger(15000000,30000000)
    nombre=fuzzy.FuzzyText()

class UserFactory(factory.DjangoModelFactory):
       FACTORY_FOR = User

       username = factory.Sequence(lambda n: "user_%d" % n)
       is_active=True
# Create your tests here.
