# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField


#TABLAS PARA LA BASE DE DATOS 
#SE CREAN DOS TABLAS (USUARIOS Y EVENTOS)
#RELACIÓN ES MUCHOS A MUCHOS 
# Create your models here.


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
    ('Incubado Tec','Incubado Tec'),('Consejero Tec','Consejero Tec'),('Empleado Tec','Empleado Tec'),('Papá/Mamá Tec','Papá/Mamá Tec'),('Ninguna','Ninguna'),)




    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 200)
    apellidos = models.CharField(max_length = 200)
    correo = models.EmailField()
    telefono = models.CharField(max_length = 200)
    sexo = models.CharField(max_length = 200,choices=SEXO_CHOICES)
    ocupacion = models.CharField(max_length = 200,choices=OCUPACION_CHOICES)
    empresa = models.CharField(max_length = 200)
    puesto =  models.CharField(max_length = 200,choices=PUESTO_CHOICES,default=None, null=True)
    estado =  models.CharField(max_length = 200,choices=ESTADO_CHOICES)
    ciudad =  models.CharField(max_length = 200)
    relacion_tec =  models.CharField(max_length = 200,choices=RELACION_TEC_CHOICES)

    class  Meta:
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.nombre
        



class Eventos(models.Model):

    TIPO_EVENTO_CHOICES=(( 'Desayuno empresarial','Desayuno empresarial'),('Taller','Taller')
    ,('Sesión de ideas que transforman','Sesión de ideas que transforman'),('Sesión informativa Incubadora','Sesión informativa Incubadora')
    ,('Sesión informativa Enlace+','Sesión informativa Enlace+')
    ,('Hackaton','Hackaton'),('Conferencia','Conferencia')
    ,('Seminario','Seminario'),('Enlace Day','Enlace Day')
    ,('BootCamp','BootCamp'),('Convocatoria','Convocatoria')
    ,('Innovation & Bussines day','Innovation & Bussines day'),('OTRO','OTRO'),)
    TIPO_INVITACION_CHOICES = (('Alumno Profesional/Preparatoria','Alumno Profesional/Preparatoria'),('Exatec','Exatec'),('Alumno Maestria Tec','Alumno Maestria Tec'),
    ('Incubado Tec','Incubado Tec'),('Consejero Tec','Consejero Tec'),('Empleado Tec','Empleado Tec'),('Papá/Mamá Tec','Papá/Mamá Tec'),('Ninguna','Ninguna'),)

    
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 300, default=None)
    imagen_portada = models.ImageField(null=False,upload_to = "portadas_eventos/%Y/%m/%D/")
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    ponentes =   models.CharField(max_length = 300)
    tipo_invitacion = MultiSelectField(choices = TIPO_INVITACION_CHOICES)
    tipo_evento = models.CharField(max_length = 200,choices=TIPO_EVENTO_CHOICES)
    concepto_pago = models.CharField(max_length = 300)

    class  Meta:
        verbose_name_plural = "Eventos"
    def __str__(self):
        return self.titulo