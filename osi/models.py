from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class tecnico(models.Model):
    nombre_del_tecnico = models.CharField(max_length=30,default=False,blank=False)
    anexo = models.CharField(max_length=6,default=None)

    def __unicode__(self):
        cadena ="{0}"
        return cadena.format(self.nombre_del_tecnico)

class formulario(models.Model):

    usuario = models.CharField(max_length=30,blank=False,null=True,default=None)
    solicitante = models.CharField(max_length=30,blank=True,default=False)
    centro_de_costo = models.CharField(max_length=30,blank=False)
    anexo = models.CharField(max_length=10,blank=False,default=False)
    asunto = models.TextField(blank=False)
    atendido_por = models.ForeignKey(tecnico,default=True,null=True)
    caso_selector= (('a','abierto'),('b','cerrado'),('c','asignado'),('d','pendiente'),('e','en proceso'))
    status_ticket= models.CharField(max_length=1,choices= caso_selector,default='c')
    fecha_inicio_ticket =models.DateTimeField(auto_now_add=False)
    fecha_solucion_ticket =models.DateTimeField(auto_now_add=False,null=True,blank=True)
    tiempo_solucion= models.CharField(max_length=10,blank=True)
    fuente_selector = (('P','C.A.U-Paipote'),('I','Informatica fomento'),('S','C.A.U-Sistemas'),('C','C.A.U'),('N','NN'))
    fuente_ticket= models.CharField(max_length=1,choices=fuente_selector,default='P')
    servicio_tecnico_selector = (('a','NN'),('b','administracion de base de datos'),('c','almacenamiento storage/fileserver'),('d','aplicaciones web'),('e','autenticacion cuentas acceso'),('f','correo electronico'),('g','data center espacio-poder-clima '),('h','desarollo Sias'),('i','internet isp'),('j','mantencion sias'),('k','mesa de servicio'),('l','monitoreo '),('m','multifuncional impresion-impresora-escaner'),('n','ofimatica estacion trabajo-software'),('o','procesamiento de datos servidores'),('p','proyeccion c/s sala'),('q','punto de red'),('r','redes MPLS wan'),('s','redes lan'),('t','respaldo y recuperacion'),('u','seguridad periometral e interna'),('v','soporte sias'),('w','telefonia ip publica movil y analoga '),('x','video conferencia/camaras'),('y','explotacion de sitemas'),('z','control automatico'))
    servicio_ti_tecnico= models.CharField(max_length=1,choices=servicio_tecnico_selector,default='a')
    servicio_cara_selector=(('a','NN'),('b','informacion para toma de decisiones'),('c','navegacion web internet-intranet '),('d','colaboracion y comunicacion'),('e','impresion fotocopiado escaner o fax'),('f','ofimatica basica puesto de trabajo'))
    servicio_ti_de_cara_al_usuario= models.CharField(max_length=1,choices=servicio_cara_selector,default='a')
    reparticion_selector =(('a','paipote'),('b','NN'),('c','antofagasta'),('d','rancagua'),('e','santiago'),('f','coquimbo'),('g','amalia'),('h','arica'),('i','barriles'),('j','cabildo'),('k','calama'),('l','camarones'),('m','catemu'),('n','copiapo'),('o','delta'),('p','el arenal'),('q','el salado'),('r','illapel'),('s','la serena'),('t','las cenizas'),('u','las luces'),('v','mantos blancos'),('w','matta'),('x','ovalle'),('y','panulcillo'),('z','rumano chileno'),('1','taltal'),('2','tocopilla'),('3','vallenar'),('4','ventanas'))
    reparticion= models.CharField(max_length=1,choices=reparticion_selector,default='a')
    medio_selector = (('a','correo'),('b','telefono'),('d','web'))
    medio_solicitud = models.CharField(max_length=1,choices=medio_selector,default='a')
    sia = models.CharField(max_length=30,blank=True)
    observacion= models.CharField(max_length=1000,blank=True)


    def NombreCompleto(self):
        cadena ="{0}----->centro de costo:{1}"
        return cadena.format(self.usuario, self.centro_de_costo, self.asunto,self.anexo,self.fecha_inicio_ticket)

    def __unicode__(self):
        return self.NombreCompleto()
