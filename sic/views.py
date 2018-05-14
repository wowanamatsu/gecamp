from django.shortcuts import render, HttpResponseRedirect, redirect

from .models import Pessoa
from .forms import FormPessoa

from .models import Pais
from .frmPais import FormPais


#=============================================================================================
def home(request):
    return render(request, 'pessoas/home.html', {})


def pessoas(request):
    dados = Pessoa.objects.all()
    return render(request, 'pessoas/index.html', {'dados':dados})




def cadastro(request):
    if request.method == 'POST':
        form = FormPessoa(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pessoas/')
    else:
        form = FormPessoa()
    return render(request, 'pessoas/cadastro.html', {'form':form})


#=============================================================================================
def cadastro_pais(request):
    paises_cadastrados = Pais.objects.all()
    if request.method == 'POST':
        form = FormPais(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/paises/')
    else:
        form = FormPais()
    return render(request, 'pais/index.html', {'form':form, 'paises':paises_cadastrados})