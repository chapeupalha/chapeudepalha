import simplejson
from django.shortcuts import render, redirect
import json
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User

from core.models import Status_Geral, Municipio
from participante.models import Participante, DocumentosParticipante, EstadoCivil, TipoDocumentoEmpregador, GrauEscolaridade, TurnoEscolar, \
    Deficiencia, Raca

from participante.forms import cadastro_participante, cadastro_dados_participante, cadastro_dados_representante_legal, \
    cadastro_copia_documentos
import datetime
from django.shortcuts import redirect
from django.db.models import Count
from django.core import serializers


def principal(request):
    active_menu = 'participante'

    total_cadastros = len(Participante.objects.all())
    cadastro_andamento = len(Participante.objects.filter(status__in=[10010100, 10010200]))
    cadastro_concluido = len(Participante.objects.filter(status__in=[10010300]))

    pendente_dados_participante = len(Participante.objects.filter(verificacao_dados_participante=False))
    pendente_representante_legal = len(Participante.objects.filter(verificacao_representante_legal=False))
    pendente_documentacao = len(Participante.objects.filter(verificacao_documentacao=False))

    return render(request, '04_participante/principal.html', locals())


def novo_cadastro(request):
    active_menu = 'participante'
    form_participante = cadastro_participante(request.POST or None)

    if request.method == 'POST':
        if form_participante.is_valid():
            status_cadastro = Status_Geral.objects.get(item='CADASTRO_USUARIO', chave='CADASTRO_BENEFICIARIO')

            form_obj = form_participante.save(commit=False)
            form_obj.status = status_cadastro

            user_password = User.objects.make_random_password(8, 'AEIOUabcdefghijklmnopqrstuvwxyz123456789'),
            new_user = User.objects.create_user(
                first_name=form_obj.nome_completo[0:30],
                username=form_obj.cpf,
                password=user_password,
            )
            new_user.save()
            form_obj.usuario = new_user
            form_obj.save()

            return redirect('/participante/cadastro/%s' % (form_obj.id))

    return render(request, '04_participante/novo_cadastro.html', locals())


def cadastro_basico(request, id_participante):
    active_menu = 'participante'
    tab_active = 'participante'
    beneficiario = Participante.objects.get(id=id_participante)

    if beneficiario.dt_nascimento:
        beneficiario.dt_nascimento = beneficiario.dt_nascimento.strftime('%d/%m/%Y')

    if beneficiario.dt_entrada:
        beneficiario.dt_entrada = beneficiario.dt_entrada.strftime('%d/%m/%Y')

    if beneficiario.dt_saida:
        beneficiario.dt_saida = beneficiario.dt_saida.strftime('%d/%m/%Y')

    form_participante = cadastro_dados_participante(request.POST or None, instance=beneficiario)

    if request.method == 'POST':
        if form_participante.is_valid():
            status_cadastro = Status_Geral.objects.get(item='CADASTRO_USUARIO', chave='CADASTRO_BENEFICIARIO_DADOS')

            form_obj = Participante.objects.get(id=id_participante)
            form_obj = form_participante.save(commit=False)
            form_obj.status = status_cadastro
            form_obj.dt_alteracao = datetime.datetime.now()
            form_obj.usuario_updated = request.user
            form_obj.verificacao_dados_participante = True

            form_obj.save()

    if beneficiario.verificacao_dados_participante and beneficiario.verificacao_representante_legal and \
            beneficiario.verificacao_documentacao:
        cadastro_completo = True

    return render(request, '04_participante/cadastro_basico.html', locals())


def cadastro_representante_legal(request, id_participante):
    active_menu = 'participante'
    tab_active = 'representante'
    beneficiario = Participante.objects.get(id=id_participante)

    if beneficiario.representante_legal_dt_nascimento:
        beneficiario.representante_legal_dt_nascimento = beneficiario.representante_legal_dt_nascimento.strftime('%d/%m/%Y')

    form_representante_legal = cadastro_dados_representante_legal(request.POST or None, instance=beneficiario)

    if request.method == 'POST':
        if form_representante_legal.is_valid():
            status_cadastro = Status_Geral.objects.get(item='CADASTRO_USUARIO', chave='CADASTRO_BENEFICIARIO_DADOS')

            form_obj = Participante.objects.get(id=id_participante)
            form_obj = form_representante_legal.save(commit=False)
            form_obj.status = status_cadastro
            form_obj.dt_alteracao = datetime.datetime.now()
            form_obj.usuario_updated = request.user
            form_obj.verificacao_representante_legal = True

            form_obj.save()

    if beneficiario.verificacao_dados_participante and beneficiario.verificacao_representante_legal and \
            beneficiario.verificacao_documentacao:
        cadastro_completo = True

    return render(request, '04_participante/cadastro_representante_legal.html', locals())


def cadastro_representante_legal_situacao(request, id_participante, status):
    active_menu = 'participante'
    beneficiario = Participante.objects.get(id=id_participante)

    status_cadastro = Status_Geral.objects.get(item='CADASTRO_USUARIO', chave='CADASTRO_BENEFICIARIO_DADOS')

    if status == 1:
        beneficiario.possui_representante_legal = True
        beneficiario.verificacao_representante_legal = False
    elif status == 0:
        beneficiario.possui_representante_legal = False
        beneficiario.verificacao_representante_legal = True
        beneficiario.representante_legal_cpf = None
        beneficiario.representante_legal_dt_nascimento = None
        beneficiario.representante_legal_nis_pis = None
        beneficiario.representante_legal_nome = None

    beneficiario.status = status_cadastro
    beneficiario.dt_alteracao = datetime.datetime.now()
    beneficiario.usuario_updated = request.user

    beneficiario.save()

    return redirect('/participante/cadastro/%s/representante' % id_participante)


def cadastro_documentos(request, id_participante):
    active_menu = 'participante'
    tab_active = 'documento'
    beneficiario = Participante.objects.get(id=id_participante)

    form_documentos = cadastro_copia_documentos(request.POST, request.FILES)

    now = datetime.datetime.now()

    if request.method == 'POST':
        if form_documentos.is_valid():
            obj_documento = DocumentosParticipante.objects.create(
                documento=form_documentos.files['documento'],
                participante=beneficiario,
                tipo_documento=form_documentos.instance.tipo_documento,
                dt_cadastro=now
            )
            obj_documento.save()

            tipo_doc = form_documentos.instance.tipo_documento.nome_bd

            if tipo_doc == 'rg':
                beneficiario.verificacao_rg = True
            elif tipo_doc == 'cpf':
                beneficiario.verificacao_cpf = True
            elif tipo_doc == 'nis':
                beneficiario.verificacao_nis = True
            elif tipo_doc == 'contrato':
                beneficiario.verificacao_contrato_trabalho = True
            elif tipo_doc == 'ctps':
                beneficiario.verificacao_ctps = True
            elif tipo_doc == 'endereco':
                beneficiario.verificacao_endereco = True

            beneficiario.save()

    if not beneficiario.verificacao_nis and not beneficiario.verificacao_contrato_trabalho and \
            not beneficiario.verificacao_ctps and not beneficiario.verificacao_cpf and \
            not beneficiario.verificacao_rg and not beneficiario.verificacao_endereco:
        nenhum_doc = True

    if beneficiario.verificacao_nis and beneficiario.verificacao_contrato_trabalho and \
            beneficiario.verificacao_ctps and beneficiario.verificacao_cpf and \
            beneficiario.verificacao_rg and beneficiario.verificacao_endereco:
        beneficiario.verificacao_documentacao = True
    else:
        beneficiario.verificacao_documentacao = False

    if beneficiario.verificacao_dados_participante and beneficiario.verificacao_representante_legal and \
            beneficiario.verificacao_documentacao:
        cadastro_completo = True

    beneficiario.save()

    return render(request, '04_participante/cadastro_documentos.html', locals())


def participante_cardsave(request, id_participante):
    active_menu = 'participante'

    if request.method == 'POST':
        if request.is_ajax():
            id_beneficiario = request.POST.get('id_particip')
            id_card = request.POST.get('codcard')

            beneficiario = Participante.objects.get(id=id_beneficiario)

            new_status = Status_Geral.objects.get(item='CADASTRO_USUARIO', chave='CADASTRO_BENEFICIARIO_COMPLETO')

            beneficiario.card_id = id_card
            beneficiario.status = new_status
            beneficiario.dt_alteracao = datetime.datetime.now()
            beneficiario.usuario_updated = request.user

            beneficiario.save()

            data = {'message': 'Cartao cadastrado'}
            return HttpResponse(json.dumps(data), content_type='application/json')

    return render(request, '04_participante/cardsave.html', locals())


def consultar_beneficiario(request):
    active_menu = 'participante'

    all_participantes = Participante.objects.all()

    if request.method == 'POST':
        print('')

    return render(request, '04_participante/consultar_beneficiario.html', locals())


def consultar_dados_beneficiario(request, id_participante):
    active_menu = 'participante'

    return render(request, '04_participante/consultar_dados_beneficiario.html', locals())


def consultar_dados_beneficiario_cartao(request):
    active_menu = 'participante'

    if request.method == 'POST':
        cartao_id = request.POST.get('cartao_id')
        beneficiario = Participante.objects.get(card_id=cartao_id)

    return redirect('/participante/cadastro/%s' % (beneficiario.id))


def ajax_chart_sexo(request):

    qsSexoMasc = len(Participante.objects.filter(sexo='M'))
    qsSexoFem = len(Participante.objects.filter(sexo='F'))
    qsSexoOutro = len(Participante.objects.filter(sexo='ND'))

    context = {
        'sexo': ['Masculino', 'Feminino', 'Outros'],
        'qtd': [qsSexoMasc, qsSexoFem, qsSexoOutro],
    }

    return HttpResponse(simplejson.dumps(context), content_type='application/json')


def ajax_chart_municipio(request):

    qs = Participante.objects.filter(verificacao_dados_participante=True).values('municipio_participante__nome').annotate(count=Count('municipio_participante')).order_by('-count')[:10]

    municipio = []
    qtd = []
    for x in qs:
        municipio.append(x['municipio_participante__nome'])
        qtd.append(x['count'])

    context = {
        'municipio': municipio,
        'qtd': qtd,
    }

    return HttpResponse(simplejson.dumps(context), content_type='application/json')


def ajax_chart_dt_cadastro(request):

    qs = Participante.objects.filter().values('dt_cadastro').annotate(count=Count('dt_cadastro')).order_by('dt_cadastro')[:20]

    dt_cadastro = []
    qtd = []

    # date_str = dt_obj.strftime("%Y-%m-%d

    for x in qs:
        dt_cadastro.append(x['dt_cadastro'].strftime("%d/%m/%Y"))
        qtd.append(x['count'])

    context = {
        'dt_cadastro': dt_cadastro,
        'qtd': qtd,
    }

    return HttpResponse(simplejson.dumps(context), content_type='application/json')
