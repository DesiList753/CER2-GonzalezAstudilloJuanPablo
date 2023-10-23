from django.shortcuts import render
from .models import Comunicado, Entidad
# Create your views here.


def index(request):
    comunicados = Comunicado.objects.filter(visible=True).order_by('fecha_publicacion')
    entidades = Entidad.objects.order_by('nombre_entidad')
    select_entidad = request.POST.get('s_entidad')
    if request.method == 'POST':
        comunicados = comunicados.filter(entidad=select_entidad)
        return render(request, 'usmweb/index.html',{'comunicados':comunicados,'entidades':entidades})
    else:
        return render(request, 'usmweb/index.html',{'comunicados':comunicados,'entidades':entidades})


#haber analiza tienes 2 variables que entregas a el html, una que es la comunicados la cual en si transportaria los comunicados ordenados