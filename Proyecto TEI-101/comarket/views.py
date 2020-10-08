from django.shortcuts import render, redirect
from .models import Foro, Mercado
from django.http import HttpResponse


def index(request):
   
    return render(request, "index.html")

def servicio(request):
    return render(request, "servicio.html")

def nosotros(request):
    return render(request, "nosotros.html")

def ods(request):
    return render(request, 'ods.html')

def formulario(request):
    return render(request, 'formulario.html')

def enviado(request):
    return render(request, 'enviado.html')