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

######################ACCOUNTS##############################





from django.shortcuts import render, redirect , HttpResponse
from django.urls import reverse


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse




def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
               form.save()
               return redirect('login')
               #return reverse('login')
               #return reverse_lazy('login')
               #return redirect(reverse('smartlink:login'))
               #return render(request,'accounts/login.html')
        else:
               return HttpResponse('You have an error while filling the form , dont forget to set more complex password')    
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('smartlink:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('smartlink:view_profile'))
        else:
            return redirect(reverse('smartlink:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


#############################################################


def home(request):


    eventos_smartlink= Eventos.objects.all()
    context = {'eventos_smartlink':eventos_smartlink}
    return render(request,'index.html',context)

def logout(request):


    eventos_smartlink= Eventos.objects.all()
    context = {'eventos_smartlink':eventos_smartlink}
    return render(request,'logout.html',context)





class SendEmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Subject')}))
    message = forms.CharField(widget=forms.Textarea)
    users = forms.ModelMultipleChoiceField(label="To",
                                           queryset=Clientes.objects.all(),
                                           widget=forms.SelectMultiple())


class SendUserEmails( FormView):
    template_name = 'send_email.html'
    form_class = SendEmailForm
#    success_url = reverse_lazy('admin:users_user_changelist')

    def form_valid(self, form):
        users = form.cleaned_data['users']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email_users.delay(users, subject, message)
        user_message = '{0} users emailed successfully!'.format(form.cleaned_data['users'].count())
        messages.success(self.request, user_message)
        return super(SendUserEmails, self).form_valid(form)