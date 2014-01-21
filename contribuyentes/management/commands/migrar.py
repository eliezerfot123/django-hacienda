from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from contribuyentes.models import *
class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--rubro',
            action='store',
            nargs=1, 
            dest='rubro',
            help='Importa rubros'),
        make_option('--contrib',action='store',nargs=1,dest='contrib',help='Importar contribuyentes'))
    def __abrir_archivo(self,nombre):
        import csv
        try:
            return csv.reader(open(nombre,'r'), delimiter=',',quotechar='"')
        except IOError:
            raise CommandError('Archivo no existe' )
    
    def __rubro(self,archivo):
        next(archivo)
        for linea in archivo:
            rubro=Rubro.objects.filter(codigo=linea[1])
            if not rubro.exists():
                print (linea)
                if linea[3] is not '':
                    alicuota=float(linea[3].replace(',','.'))
                else:
                    alicuota=0
                Rubro(codigo=linea[1],rubro=linea[2],alicuota=alicuota,ut=linea[4]).save()
        self.stdout.write('Successfully closed poll' )

    def __contribuyente(self,archivo):
        #for n in range(24000):
        next(archivo)
        for linea in archivo:
            print (linea)

            if not Contribuyente.objects.filter(num_identificacion=linea[1]).exists():
                if linea[7]=='':
                    linea[7]=0.0
                else:
                    linea[7]=linea[7].replace(',','.')
                    if linea[7][-3:]=='.00':
                        linea[7]=linea[7][:-3] 
                    if linea[7].find('MENOS')-1:
                        linea[7]='999'
                fecha=linea[13].split('/')
                linea[13]=fecha[2]+"-"+fecha[1]+"-"+fecha[0]


                contribuyente=Contribuyente(id_contrato=linea[0],num_identificacion=linea[1],nombre=linea[2],telf=linea[3],fax=linea[4],representante=linea[5],cedula_rep=linea[6],capital=linea[7],direccion=linea[11],modificado=linea[13])
                contribuyente.save()
                if linea[12] !='' and 'DESINCOR' not in linea[12] and 'desincor' not in linea[12] and 'INACTIV' not in linea[12] and 'INHABILITAD' not in linea[12] and 'AGENTE' not in linea[12]:
                    sep='-'
                    if len(linea[12].split(','))>1:
                        sep=','

                    for rubros in linea[12].split(sep):

                        rubro=Rubro.objects.filter(codigo=rubros)
                        if rubro.exists():
                            rubro=rubro[0]
                            contribuyente.rubro.add(rubro)


            
            else:
                print ("Contribuyente ya existe",linea[1])

    def handle(self, *args, **options):
        if options['rubro']is not None:
            nombre=options['rubro']
            archivo=self.__abrir_archivo(nombre)
            self.__rubro(archivo)
        elif options['contrib']is not None: 
            
            nombre=options['contrib']
            archivo=self.__abrir_archivo(nombre)
            self.__contribuyente(archivo)
            




