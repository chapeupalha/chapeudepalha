from django.shortcuts import render

from atividade.models import Trabalho_campo

from atividade.forms import cadastro_atividade_trabalho

def home_atividade(request):

    return render(request, '05_atividade/home.html', locals())


def cadastro(request):
    form_atividade = cadastro_atividade_trabalho(request.POST or None)

    if request.method == 'POST':
        if form_atividade.is_valid():
            print('teste')

    return render(request, '05_atividade/cadastro.html', locals())