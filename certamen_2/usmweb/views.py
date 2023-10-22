from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado, Entidad
# Create your views here.


def base(request):
    
    return render(request, 'usmweb/base.html')


def filtro(request):


    return render(request, 'usmweb/filtro.html')