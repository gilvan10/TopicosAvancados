from django.shortcuts import render
from django.http import HttpResponse
from . import urls

# Create your views here.

def index(request):
    return HttpResponse("Olá, Mundo. Você está na página index de clsapi")

def estabelecimento(request):
    return render(request, 'clspai/estabelecimeto.html', {})

def marca(request):
    return render(request, 'clspai/marca.html', {})

def unidade(request):
    return render(request, 'clspai/unidade.html', {})

def filtro(request):
    return render(request, 'clspai/filtro.html', {})
