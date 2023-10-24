from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado, Entidad
# Create your views here.   


def index(request):
    comunicados = Comunicado.objects.order_by('fecha_publicacion')
    entidades = Entidad.objects.order_by('nombre_entidad')
    select_entidad = request.GET.get('s_entidad')
    if select_entidad:
        comunicados = comunicados.filter(entidad=select_entidad)
    return render(request, 'usmweb/index.html', {'comunicados': comunicados, 'entidades': entidades})
#si uso data en el html voy a enredarme
