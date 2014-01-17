from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from contribuyentes.models import Rubros
class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--rubro',
            action='store',
            nargs=1, 
            dest='rubro',
            help='Importa rubros'),
        )
    def _abrir_archivo(self,nombre):
        import csv
        try:
            return csv.reader(open(nombre,'rb'), delimiter=',',quotechar='"')
        except IOError:
            raise CommandError('Archivo no existe' )

    def handle(self, *args, **options):
        if options['rubro']<> '':
            nombre=options['rubro']
            archivo=self._abrir_archivo(nombre)
            archivo.next()
            for linea in archivo:
                rubro=Rubros.objects.filter(codigo=linea[1])
                if not rubro.exists():
                    print linea
                    if linea[3]<>'':
                        alicuota=float(linea[3].replace(',','.'))
                    else:
                        alicuota=0
                    Rubros(codigo=linea[1],rubro=linea[2],alicuota=alicuota,ut=linea[4]).save()



            self.stdout.write('Successfully closed poll' )
