from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado, Entidad
# Create your views here.


def base(request):
    entidad = Entidad.objects.all()
    return render(request, 'usmweb/base.html')


def filtro(request):
    Comunicados = Comunicado.objects.all()

    return render(request, 'usmweb/filtro.html')