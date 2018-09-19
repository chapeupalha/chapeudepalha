from django.shortcuts import render, redirect
import datetime

from atividade.models import Trabalho_campo, Ocorrencia, Tarefa_correncia
from core.models import Status_Geral

from atividade.forms import cadastro_atividade_trabalho, cadastro_ocorrencia_form, cadastro_solucao_form
from atividade.utils import generate_protocolo


def home_atividade(request):

    atividades_cadastradas = Trabalho_campo.objects.all()
    status_atividade = Status_Geral.objects.filter(item='ATIVIDADE_TRABALHO')

    atividade_andamento = atividades_cadastradas.filter(at_status_id=20010100).count()
    atividade_encerrada = atividades_cadastradas.filter(at_status_id=20020100).count()
    atividade_cancelada = atividades_cadastradas.filter(at_status_id=20011111).count()

    return render(request, '05_atividade/home.html', locals())


def cadastro_atividade(request):
    form_atividade = cadastro_atividade_trabalho(request.POST or None)

    if request.method == 'POST':
        if form_atividade.is_valid():
            status_atividade = Status_Geral.objects.get(item='ATIVIDADE_TRABALHO', chave='CADASTRO_ATIVIDADE_ANDAMENTO')
            form_atividade = form_atividade.save(commit=False)

            form_atividade.at_status = status_atividade
            form_atividade.save()

            return redirect('/atividade')

    return render(request, '05_atividade/cadastro.html', locals())


def home_ocorrencia(request):

    all_ocorrencia = Ocorrencia.objects.all()

    if request.method == 'POST':
        print('teste')

    return render(request, '06_ocorrencia/home.html', locals())


def cadastro_ocorrencia(request):
    form_ocorrencia = cadastro_ocorrencia_form(request.POST or None)

    if request.method == 'POST':
        if form_ocorrencia.is_valid():
            status_ocorrencia = Status_Geral.objects.get(item='OCORRENCIA_PROJETO', chave='CADASTRO_OCORRENCIA_INICIAL')
            now = datetime.datetime.now()

            form_orcorrencia = form_ocorrencia.save(commit=False)
            form_orcorrencia.num_protocolo = generate_protocolo()
            form_orcorrencia.dt_solicitacao = now
            form_orcorrencia.user_atendente = request.user
            form_orcorrencia.status = status_ocorrencia

            form_orcorrencia.save()
            return redirect('/atividade/ocorrencia/%s/consulta' % (form_orcorrencia.id,))

    return render(request, '06_ocorrencia/cadastro.html', locals())


def consulta_ocorrencia(request, id_ocorrencia):
    ocorrencia_cadastrada = Ocorrencia.objects.get(id=id_ocorrencia)
    solucao_cadastrada = Tarefa_correncia.objects.filter(ocorrencia=ocorrencia_cadastrada)

    return render(request, '06_ocorrencia/consulta_ocorrencia.html', locals())


def solucao_ocorrencia(request, id_ocorrencia):
    ocorrencia_cadastrada = Ocorrencia.objects.get(id=id_ocorrencia)
    form_solucao = cadastro_solucao_form(request.POST or None)

    if request.method == 'POST':
        if form_solucao.is_valid():
            status_ocorrencia = Status_Geral.objects.get(item='OCORRENCIA_PROJETO', chave='OCORRENCIA_SOLUCAO_CADASTRADA')
            now = datetime.datetime.now()

            form_solucao = form_solucao.save(commit=False)
            form_solucao.ocorrencia = ocorrencia_cadastrada
            form_solucao.save()

            Ocorrencia.objects.filter(id=id_ocorrencia).update(status=status_ocorrencia)

            return redirect('/atividade/ocorrencia/%s/consulta' % (ocorrencia_cadastrada.id,))


    return render(request, '06_ocorrencia/solucao_ocorrencia.html', locals())


def finalizar_ocorrencia(request, id_ocorrencia):
    ocorrencia_cadastrada = Ocorrencia.objects.get(id=id_ocorrencia)
    solucao_cadastrada = Tarefa_correncia.objects.filter(ocorrencia=ocorrencia_cadastrada).count()
    status_ocorrencia = Status_Geral.objects.get(item='OCORRENCIA_PROJETO', chave='OCORRENCIA_FINALIZADA')

    if solucao_cadastrada > 0:
        Ocorrencia.objects.filter(id=id_ocorrencia).update(status=status_ocorrencia)
        return redirect('/atividade/ocorrencia/')
    else:
        return redirect('/atividade/ocorrencia/%s/consulta' % (ocorrencia_cadastrada.id,))

    return render(request, '06_ocorrencia/consulta_ocorrencia.html', locals())
