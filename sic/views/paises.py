from django.shortcuts import render, redirect

from sic.models import Pais
from sic.forms.pais import FormPais


def cadastro_pais(request):
    paises_cadastrados = Pais.objects.all()
    if request.method == 'POST':
        form = FormPais(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/paises/')
    else:
        form = FormPais()
    return render(request, 'paises/index.html', {'form':form, 'paises':paises_cadastrados})