from django.shortcuts import render
from django.http import HttpResponse
from .models import Estabelecimento
from .models import Marca
from .models import Unidade
from .models import Filtro
from django.shortcuts import redirect
from . import urls
from .formsEstabelecimento import EstabelecimentoForm
from .formsFiltro import FiltroForm
from .formsMarca import MarcaForm
from .formsUnidade import UnidadeForm

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

def estabelecimento_new(request):
    if request.method == "POST":
        estabelecimento = EstabelecimentoForm(request.POST)
        if estabelecimento.is_valid():
           estabecimentoExtra = estabelecimento.save(commit=False)
           estabelecimento.descricao = request.descricao
           estabelecimento.localizacao = request.localizacao
           estabecimentoExtra.save()
           return redirect('estabelecimento_detail', pk=estabelecimento.pk)
        else:
            estabelecimento = EstabelecimentoForm()
            return render(request, 'clsapi/estabelecimento_edit.html', {'estabelecimento': estabelecimento})

def filtro_new(request):
    if request.method == "POST":
        filtro = FiltroForm(request.POST)
        if filtro.is_valid():
           filtroExtra = filtro.save(commit=False)
           filtro.descricao = request.descricao
           filtroExtra.save()
           return redirect('filtro_detail', pk=filtro.pk)
        else:
            filtro = FiltroForm()
            return render(request, 'clsapi/filtro_edit.html', {'filtro': filtro})

def marca_new(request):
    if request.method == "POST":
        marca = MarcaForm(request.POST)
        if marca.is_valid():
            marcaExtra = marca.save(commit=False)
            marca.descricao = request.descricao
            marcaExtra.save()
            return redirect('marca_detail', pk=marca.pk)
        else:
            marca = MarcaForm()
            return render(request, 'clsapi/marca_edit.html', {'marca': marca})

def unidade_new(request):
    if request.method == "POST":
        unidade = UnidadeForm(request.POST)
        if unidade.is_valid():
            unidadeExtra = unidade.save(commit=False)
            unidade.descricao = request.descricao
            unidadeExtra.save()
            return redirect('unidade_detail', pk=unidade.pk)
        else:
            unidade = UnidadeForm()
            return render(request, 'clsapi/unidade_edit.html', {'unidade': unidade})

def estabelecimento_detail(request):

def filtro_detail(request):

def marca_detail(request):

def unidade_detail(request):

def estabelecimento_edit(request, pk):
    estabelecimento = get_object_or_404(Estabelecimento, pk=pk)
    if request.method == "POST":
        estabelecimentoExtra = EstabelecimentoForm(request.POST, instance=estabelecimento)
        if estabelecimentoExtra.is_valid():
            estabelecimento = estabelecimentoExtra.save(commit=False)
            livro.save()
            return redirect('estabelecimento_detail', pk=estabelecimento.pk)
    else:
        estabelecimentoExtra = EstabelecimentoForm(instance=estabelecimento)
        return render(request, 'clsapi/estabelecimento_edit.html', {'estabelecimentoExtra': estabelecimentoExtra})

def filtro_edit(request, pk):
    filtro = get_object_or_404(Filtro, pk=pk)
    if request.method == "POST":
        filtroExtra = FiltroForm(request.POST, instance=filtro)
        if filtroExtra.is_valid():
            filtro = filtroExtra.save(commit=False)
            filtro.save()
            return redirect('filtro_detail', pk=filtro.pk)
    else:
        filtroExtra = EstabelecimentoForm(instance=filtro)
        return render(request, 'clsapi/filtro_edit.html', {'filtroExtra': filtroExtra})

def marca_edit(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        marcaExtra = MarcaForm(request.POST, instance=marca)
        if marcaExtra.is_valid():
            marca = marcaExtra.save(commit=False)
            marca.save()
            return redirect('marca_detail', pk=marca.pk)
    else:
        marcaExtra = MarcaForm(instance=marca)
        return render(request, 'clsapi/marca_edit.html', {'marcaExtra': marcaExtra})

def unidade_edit(request, pk):
    unidade = get_object_or_404(Unidade, pk=pk)
    if request.method == "POST":
        unidadeExtra = UnidadeForm(request.POST, instance=unidade)
        if unidadeExtra.is_valid():
            unidade = unidadeExtra.save(commit=False)
            unidade.save()
            return redirect('unidade_detail', pk=unidade.pk)
    else:
        unidadeExtra = UnidadeForm(instance=unidade)
        return render(request, 'clsapi/unidade_edit.html', {'unidadeExtra': unidadeExtra})

def estabelecimento_delete(request, pk):
    estabelecimento = get_object_or_404(Estabelecimento, pk=pk)
    if request.method == "POST":
        estabelecimento.delete()
        #esse estabelecimento é se referindo a lista de estabelecimentos
        return redirect('estabelecimento')
    else:
        estabelecimentoExtra = EstabelecimentoForm(instance=estabelecimento)
        return render(request, 'clsapi/estabelecimento_delete.html', {'estabelecimento': estabelecimento})

def filtro_delete(request, pk):
    filtro = get_object_or_404(Filtro, pk=pk)
    if request.method == "POST":
        filtro.delete()
        #esse filtro é se referindo a lista de filtros
        return redirect('filtro')
    else:
        filtroExtra = FiltroForm(instance=filtro)
        return render(request, 'clsapi/filtro_delete.html', {'filtro': filtro})

def marca_delete(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        marca.delete()
        #esse marca é se referindo a lista de marcas
        return redirect('marca')
    else:
        marcaExtra = MarcaForm(instance=marca)
        return render(request, 'clsapi/marca_delete.html', {'marca': marca})

def unidade_delete(request, pk):
    unidade = get_object_or_404(Unidade, pk=pk)
    if request.method == "POST":
        unidade.delete()
        #esse unidade é se referindo a lista de unidades
        return redirect('unidade')
    else:
        unidadeExtra = UnidadeForm(instance=unidade)
        return render(request, 'clsapi/unidade_delete.html', {'unidade': unidade})


