# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import FormView
from django.shortcuts import render
from .models import *
from django import *
from django.utils.translation import gettext as _
# Create your views here.
from django import forms

def home(request):


    eventos_smartlink= Eventos.objects.all()
    context = {'eventos_smartlink':eventos_smartlink}
    return render(request,'index.html',context)

def login(request):

    return render(request,'login.html')



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