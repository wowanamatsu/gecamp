from django.shortcuts import render, HttpResponseRedirect

from .models import Pessoa
from .forms import FormPessoa


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
