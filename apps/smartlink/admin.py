# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group, AbstractUser
from django.contrib.admin.models import LogEntry
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from django.contrib.auth.models import Permission
from django.core.mail import send_mail
from django import forms
from .forms import *
from django.shortcuts import render
############




class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ('nombre','apellidos','telefono_celular','sexo','ocupacion','estado','relacion_tec','get_eventos')
    list_filter  = ('ocupacion','relacion_tec')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-nombre', 'user')
        return queryset

    user_info.short_description = 'Info'


    actions =['send_email']



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


    def send_email(self, request, queryset):
        form = SendEmailForm(initial={'users': queryset})
        
        return render(request, 'send_email.html', {'form': form})

admin.site.register(Clientes, UserProfileAdmin)
############





'''



class SendEmailForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ('Subject')}))
    message = forms.CharField(widget=forms.Textarea)
    users = forms.ModelMultipleChoiceField(label="To",
                                           queryset=User.objects.all(),
                                           widget=forms.SelectMultiple())

def send_email(self, request, queryset):
    for i in queryset:
        if i.correo:
            send_mail('Invitacion a ', 'Cuerpo de mensaje', 'from@example.com',[i.correo], fail_silently=False)
        else:
            self.message_user(request, "Correos enviados!") 
send_email.short_description = "Enviar correo a los usuarios seleccionados"
'''
#LogEntry.objects.all().delete()

#admin.site.unregister(Group)
# Register your models here.
class eventos_tabla(ImportExportModelAdmin):
    date_hierarchy = 'fecha'
    list_display = ('titulo','fecha','tipo_evento','tipo_invitacion','get_registros')
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
    list_display = ('nombre','apellidos','correo','telefono_celular','sexo','ocupacion','estado','relacion_tec')
    list_filter  = ('ocupacion','relacion_tec')
    actions =['send_email']



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


    def send_email(self, request, queryset):
        form = SendEmailForm(initial={'users': queryset})
        return render(request, 'users/send_email.html', {'form': form})

#admin.site.register(Clientes,clientes_tabla)
admin.site.register(Eventos,eventos_tabla)


admin.site.index_title = ""