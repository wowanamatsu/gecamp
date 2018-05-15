from django.shortcuts import render, redirect

from sic.models import Pais
from sic.forms.pais import FormPais


def index(request):
    paises_cadastrados = Pais.objects.all()
    return render(request, 'paises/index.html', {'paises':paises_cadastrados})


def cadastro(request):
    
    if request.method == 'POST':
        form = FormPais(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/paises/')
    else:
        form = FormPais()
    return render(request, 'paises/form.html', {'form':form})