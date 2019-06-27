# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField
from tinymce import models as tinymce_models

#TABLAS PARA LA BASE DE DATOS
#SE CREAN DOS TABLAS (USUARIOS Y EVENTOS)
#RELACIÓN ES MUCHOS A MUCHOS
# Create your models here.


from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Eventos(models.Model):

    TIPO_EVENTO_CHOICES=(( 'Desayuno empresarial','Desayuno empresarial'),('Taller','Taller')
    ,('Sesión de ideas que transforman','Sesión de ideas que transforman'),('Sesión informativa Incubadora','Sesión informativa Incubadora')
    ,('Sesión informativa Enlace+','Sesión informativa Enlace+')
    ,('Hackaton','Hackaton'),('Conferencia','Conferencia')
    ,('Seminario','Seminario'),('Enlace Day','Enlace Day')
    ,('BootCamp','BootCamp'),('Convocatoria','Convocatoria')
    ,('Innovation & Bussines day','Innovation & Bussines day'),('OTRO','OTRO'),)
    TIPO_INVITACION_CHOICES = (('Alumno Profesional/Preparatoria','Alumno Profesional/Preparatoria'),('Exatec','Exatec'),('Alumno Maestria Tec','Alumno Maestria Tec'),
    ('Incubado Tec','Incubado Tec'),('Consejero Tec','Consejero Tec'),('Empleado Tec','Empleado Tec'),('Padre/Madre Tec','Padre/Madre Tec'),('General','General'),)
    PRIORIDAD = (('alta','alta'),('normal','normal'),('ninguna','ninguna'))


    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 300, default=None)
    imagen_portada = models.ImageField(null=False,upload_to = "portadas_eventos")
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    lugar = models.CharField(max_length = 300, default=None)
    ponentes =   models.CharField(max_length = 300)
    tipo_invitacion = MultiSelectField(choices = TIPO_INVITACION_CHOICES,default=None)
    #tipo_invitacion = models.CharField(max_length = 200,choices=TIPO_INVITACION_CHOICES,default=None)
    tipo_evento = models.CharField(max_length = 200,choices=TIPO_EVENTO_CHOICES)
    concepto_pago = models.CharField(max_length = 300)
    registros = models.ManyToManyField(User, blank = True)
    prioridad = models.CharField(max_length = 200,choices=PRIORIDAD,default=None)
    
    
    def get_registros(self):
        return " , ".join([str(p) for p in self.registros.all()])
    get_registros.short_description = "registros"
    

    
    class  Meta:
        verbose_name_plural = "Eventos"
    def __str__(self):
        return self.titulo

class Clientes(models.Model):
    SEXO_CHOICES = (('M','M'),('F','F'),)
    OCUPACION_CHOICES = (('Sector Empresarial','Sector Empresarial'),('Empresa propia','Empresa propia'),
    ('Sector Educación','Sector Educación'),('Sector Gubernamental','Sector Gubernamental'),('Estudiante','Estudiante'),
    ('ONG','ONG'),('No trabajo','No trabajo'),)
    PUESTO_CHOICES = (('Presidente','Presidente'),('CEO','CEO'),('Founder','Founder'),('Socio(a)','Socio(a)')
    ,('Rector','Rector'),('Director(a)','Director(a)'),('Subdirector(a)','Subdirector(a)'),('Gerente','Gerente')
    ,('Subgerente','Subgerente'),('Coordinador(a)','Coordinador(a)'),('Supervisor(a)','Supervisor(a)'),('Consultor(a)','Consultor(a)')
    ,('Contador(a)','Contador(a)'),('Investigador(a)','Investigador(a)'),('Asesor(a)','Asesor(a)'),('Contralor(a)','Contralor(a)')
    ,('Lider de proyecto','Lider de proyecto'),('Estudiante','Estudiante'),('Perito','Perito'),('Distribuidor(a)','Distribuidor(a)')
    ,('Gestor(a)','Gestor(a)'),('Abogado(a)','Abogado(a)'),('Conductor(a)','Conductor(a)'),('Diseñador(a)','Diseñador(a)')
    ,('Secretario(a)','Secretario(a)'),('Docente','Docente'),('Diputado(a)','Diputado(a)'),('Vendedor(a)','Vendedor(a)')
    ,('Delegado(a)','Delegado(a)'),('Coach','Coach'),('Capitán','Capitán'),('Superintendente','Superintendente')
    ,('Ninguno','Ninguno'),('Independiente','Independiente'),)


    ESTADO_CHOICES = (('Aguascalientes','Aguascalientes'),('Baja California','Baja California'),('Baja California Sur','Baja California Sur'),('Campeche','Campeche'),
    ('Coahuila','Coahuila'),('Colima','Colima'),('Chiapas','Chiapas'),('Chihuahua','Chihuahua'),
    ('Distrito Federal','Distrito Federal'),('Durango','Durango'),('Guanajuato','Guanajuato'),('Guerrero','Guerrero'),
    ('Hidalgo','Hidalgo'),('Jalisco','Jalisco'),('México','México'),('Michoacán','Michoacán'),
    ('Morelos','Morelos'),('Nayarit','Nayarit'),('Nuevo León','Nuevo León'),('Oaxaca','Oaxaca'),
    ('Puebla','Puebla'),('Querétaro','Querétaro'),('Quintana Roo','Quintana Roo'),('San Luis Potosí','San Luis Potosí'),
    ('Sinaloa','Sinaloa'),('Sonora','Sonora'),('Tabasco','Tabasco'),('Tamaulipas','Tamaulipas'),
    ('Tlaxcala','Tlaxcala'),('Veracruz','Veracruz'),('Yucatán','Yucatán'),('Zacatecas','Zacatecas'),
    )
    RELACION_TEC_CHOICES = (('Alumno Profesional/Preparatoria','Alumno Profesional/Preparatoria'),('Exatec','Exatec'),('Alumno Maestria Tec','Alumno Maestria Tec'),
    ('Incubado Tec','Incubado Tec'),('Consejero Tec','Consejero Tec'),('Empleado Tec','Empleado Tec'),('Padre/Madre Tec','Padre/Madre Tec'),('Ninguna','Ninguna'),('Exatec y Alumno Profesional/Preparatoria','Exatec y Alumno Profesional/Preparatoria'),
    ('Exatec y Alumno Maestria Tec','Exatec y Alumno Maestria Tec'),('Exatec e Incubado Tec','Exatec e Incubado Tec'),('Exatec y Consejero Tec','Exatec y Consejero Tec'),('Exatec y Empleado Tec','Exatec y Empleado Tec'),
    ('Exatec y Padre/Madre Tec','Exatec y Padre/Madre Tec'),('Incubado Tec y Consejero Tec','Incubado Tec y Consejero Tec'),('Incubado Tec y Empleado Tec','Incubado Tec y Empleado Tec'),)





    on_delete=models.DO_NOTHING
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True,unique=True, error_messages={'unique':"This email has already been registered."})
    
    ############
    eventos = models.ManyToManyField(Eventos, blank = True)
    
    ############
    nombre = models.CharField(max_length = 200,default=None,blank=True,null=True)
    apellidos = models.CharField(max_length = 200,default=None,null=True)
    correo = models.EmailField(default=None,null=True)
    telefono_celular =models.CharField(max_length = 200,default=None,blank=True,null=True)
    telefono_oficina = models.CharField(max_length = 200,default=None,blank=True,null=True)
    sexo = models.CharField(max_length = 200,choices=SEXO_CHOICES,default=None,null=True)
    ocupacion = models.CharField(max_length = 200,choices=OCUPACION_CHOICES,default=None,null=True)
    empresa = models.CharField(max_length = 200,default=None,null=True)
    puesto =  models.CharField(max_length = 200,choices=PUESTO_CHOICES, null=True)
    estado =  models.CharField(max_length = 200,choices=ESTADO_CHOICES,default=None,null=True)
    ciudad =  models.CharField(max_length = 200,default=None,null=True)
    relacion_tec =  models.CharField(max_length = 200,choices=RELACION_TEC_CHOICES,default=None,null=True)
    #correo = tinymce_models.HTMLField()
    



    
    def get_eventos(self):
        return " , ".join([str(p) for p in self.eventos.all()])
    

    

    
    objects = models.Manager()

    class  Meta:
        verbose_name_plural = "Clientes"


    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Clientes.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
