from django.shortcuts import render
from django.http import HttpResponse
from .models import Estabelecimento
from .models import Marca
from .models import Unidade
from .models import Filtro

from . import urls

# Create your views here.

def index(request):
    return HttpResponse("Olá, Mundo. Você está na página index de clsapi")

def estabelecimento(request):
    estabelecimento = Estabelecimento.objects.order_by('descricao')
    return render(request, 'clspai/estabelecimeto.html', {'clsapi': clsapi})

def marca(request):
    marca = Marca.objects.order_by('descricao')
    return render(request, 'clspai/marca.html', {'clsapi': clsapi})

def unidade(request):
    unidade = Unidade.objects.order_by('descricao')
    return render(request, 'clspai/unidade.html', {'clsapi': clsapi})

def filtro(request):
    filtro = Filtro.objects.order_by('descricao')
    return render(request, 'clspai/filtro.html', {'clsapi': clsapi})
