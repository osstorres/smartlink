# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats


#LogEntry.objects.all().delete()

admin.site.unregister(Group)
# Register your models here.
class eventos_tabla(ImportExportModelAdmin):
    date_hierarchy = 'fecha'
    list_display = ('titulo','fecha','tipo_evento')
    list_filter  = ('tipo_evento','fecha')
    def get_export_formats(self):
        formats = (
                base_formats.CSV,
                base_formats.XLS,

            )
        return [f for f in formats if f().can_export()]
    def get_import_formats(self):
        formats = (
                base_formats.CSV,
                base_formats.XLS,

            )
        return [f for f in formats if f().can_import()]




class clientes_tabla(ImportExportModelAdmin):
    list_display = ('nombre','apellidos','correo','telefono','sexo','ocupacion','estado','relacion_tec')
    list_filter  = ('ocupacion','relacion_tec')


    def get_export_formats(self):
        formats = (
                base_formats.CSV,
                base_formats.XLS,

            )

        return [f for f in formats if f().can_export()]
    def get_import_formats(self):
        formats = (
                base_formats.CSV,
                base_formats.XLS,

            )
        return [f for f in formats if f().can_import()]






admin.site.register(Clientes,clientes_tabla)
admin.site.register(Eventos,eventos_tabla)

admin.site.index_title = ""