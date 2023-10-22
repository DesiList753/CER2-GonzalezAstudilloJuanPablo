from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado, Entidad
# Create your views here.



def index(request):

    return render(request, 'usmweb/index.html')