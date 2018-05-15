from django.shortcuts import render, HttpResponseRedirect, redirect

from sic.models import Pessoa
from sic.forms.pessoa import FormPessoa

from sic.models import Pais

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
    return render(request, 'pessoas/form.html', {'form':form})


