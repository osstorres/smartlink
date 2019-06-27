# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import FormView
from django.shortcuts import render
from .models import *
from django import *
from django.utils.translation import gettext as _
# Create your views here.
from django import forms
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from django.core.mail import send_mail
from django.template.loader import get_template

######################ACCOUNTS##############################
import datetime



from django.contrib import messages
from django.shortcuts import render, redirect , HttpResponse
from django.urls import reverse


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives



def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        #profile_form = ClienteForm(request.POST)7

        
        if form.is_valid(): #and profile_form.is_valid():
               username = form.cleaned_data.get("username")
               print("USUARIO REGISTRO:", username)
               form.save()
           
               
               
               return redirect('login')
               #return reverse('login')
               #return reverse_lazy('login')
               #return redirect(reverse('smartlink:login'))
               #return render(request,'accounts/login.html')
        else:
            username = form.cleaned_data.get("username")
            print("USUARIO REGISTRO fallidooo papppuuuuu:", username)
            form = RegistrationForm()
            print ("valido dentro del 1")
            print ("ERRORE DENTRO DE 1 : "  )
            error = True
         
            
            args = {'form': form,'error':error}
            return render(request, 'accounts/reg_form.html', args)
   
    else:
        form = RegistrationForm()
        print ("valido dentro del 2")
        print ("ERRORE DENTRO DE 2 : " )
         
        args = {'form': form}
      
        return render(request, 'accounts/reg_form.html',args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        
        
        
    else:
        user = request.user
        print("CORREO USUARIO: " ,request.user.email)
        request.user.clientes.correo = request.user.email
        print("CORREO CLIENTE :", request.user.clientes.correo)
        
        
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    request.user.clientes.correo = request.user.email
    request.user.clientes.nombre = request.user.first_name
    request.user.clientes.apellidos = request.user.last_name
 
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ClienteForm(request.POST, instance=request.user.clientes)

        if form.is_valid() and profile_form.is_valid():
            
         
            form.save()
            profile_form.save()
            #return render(request,"accounts/profile.html",{})
            return redirect('view_profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ClienteForm(instance=request.user.clientes)
        args = {'form': form,'profile_form':profile_form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return render(request,'accounts/profile.html')
        else:
            return render(request,'accounts/change_password.html')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


#############################################################


def home(request):


    eventos_smartlink= Eventos.objects.all()
    for i in eventos_smartlink:
        print("MI INVITACION",i.tipo_invitacion)
        
    


    context = {'eventos_smartlink':eventos_smartlink}


    return render(request,'index.html',context)

def historial(request):
    datenow = datetime.datetime.now()
    datenow2 = datetime.datetime.today()
    args = {'datenow':datenow}
    print("mi fecha actual " ,datenow,datenow2)

    return render(request, 'historial.html',args)


def nosotros(request):
    
    eventos_smartlink= Eventos.objects.all()

    
    context = {'eventos_smartlink':eventos_smartlink,'date_now':datetime.datetime.now()}


    return render(request,'nosotros.html',context)

def logout(request):


    eventos_smartlink= Eventos.objects.all()
    context = {'eventos_smartlink':eventos_smartlink}
    return render(request,'logout.html',context)


def evento(request, pk=None):
    if pk:
        evento = Eventos.objects.get(pk=pk)
        

    args = {'evento': evento}
    return render(request, 'evento.html', args)


def agregareventoacliente(request, pk=None):
    if pk:
        evento = Eventos.objects.get(pk=pk)
    
        #user = User.objects.get(pku=pku)  
        #context = {'eventosss':eventosss}
    request.user.clientes.eventos.add(evento.id)

    evento.registros.add(request.user.id)
    

    cuerpo_mensaje = "REGISTRO EXITOSO AL EVENTO : "+ evento.titulo +"\nFECHA :" +str(evento.fecha) + "\nLUGAR: "+evento.lugar+"\n\nNO responda a este mensaje, es un envío automático\n\n"
    send_mail('Confirmación evento',cuerpo_mensaje,'Tecnológico de Monterrey en Cuernavaca',[request.user.email],fail_silently=False)

    

        
        
        #User.empresa.add(eventosss)
        #User.clientes.save()

    #return render(request, 'historial.html')
    return redirect('historial')
















def quitarevento(request, pk=None):
    print("-----------------------ESTA COSITA-----------------------------")
    print(request.user.clientes.eventos)
    
    print("-----------------------ESTA COSITA-----------------------------")
    if pk:
        evento = Eventos.objects.get(pk=pk)
    print("-----------------------ESTA COSITA-----------------------------")
    print(request.user.clientes.eventos)
    
    print("-----------------------ESTA COSITA-----------------------------")
        #user = User.objects.get(pku=pku)  
        #context = {'eventosss':eventosss}
    request.user.clientes.eventos.remove(evento.id)
    print("-----------------------ESTA COSITA-----------------------------")
    print(request.user.clientes.eventos)
    
    print("-----------------------ESTA COSITA-----------------------------")
        
        
        #User.empresa.add(eventosss)
        #User.clientes.save()

    return render(request, 'historial.html')



'''

class SendEmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Subject')}))
    message = forms.CharField(widget=forms.Textarea)
    users = forms.ModelMultipleChoiceField(label="To",
                                           queryset=Clientes.objects.all(),
                                           widget=forms.SelectMultiple())
'''

class SendUserEmails(FormView):
    template_name = 'send_email.html'
    form_class = SendEmailForm
    #success_url = reverse_lazy('admin:users_user_changelist')

    def form_valid(self, form):
        users = form.cleaned_data['users']
        subject = form.cleaned_data['asunto']
        message = form.cleaned_data['mensaje']
        html_content = message
        
        for x in users:
            print(x.correo)
            #send_mail(subject, message,'smartlink',[x.correo],fail_silently=False)


            subject, from_email, to = subject, 'Tecnológico de Monterrey en Cuernavaca <do_not_reply@tec.com>', x.correo
            text_content = 'This is an important message.'
            
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content,"text/html")
            msg.send()
        
        
        #send_mail('Confirmación evento',cuerpo_mensaje,'SMART LINK',[request.user.email],fail_silently=False)
        return HttpResponseRedirect('/admin')