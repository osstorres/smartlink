# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):


    eventos_smartlink= Eventos.objects.all()
    context = {'eventos_smartlink':eventos_smartlink}
    return render(request,'index.html',context)