from django.shortcuts import render
from .models import Service #en este momento ya he importado mi modelo de datos

# Create your views here.

def services(request) :
    servicios = Service.objects.all()
    return render(request, 'servicios/services.html', {'services' : servicios})
