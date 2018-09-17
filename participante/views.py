from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from core.models import Status_Geral
from participante.models import Participante

from participante.forms import cadastro_participante, cadastro_dados_participante


def cadastro(request):

    return render(request, '04_participante/cadastro.html', locals())


def novo_cadastro(request):
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
    tab_active = 'participante'
    beneficiario = Participante.objects.get(id=id_participante)

    form_participante = cadastro_dados_participante(request.POST or None, instance=beneficiario)

    return render(request, '04_participante/cadastro_basico.html', locals())


def cadastro_representante_legal(request, id_participante):
    tab_active = 'representante'
    beneficiario = Participante.objects.get(id=id_participante)
    return render(request, '04_participante/cadastro_representante_legal.html', locals())


def cadastro_documentos(request, id_participante):
    tab_active = 'documento'
    beneficiario = Participante.objects.get(id=id_participante)
    return render(request, '04_participante/cadastro_documentos.html', locals())


def consultar_beneficiario(request):

    all_participantes = Participante.objects.all()

    return render(request, '04_participante/consultar_beneficiario.html', locals())


def consultar_dados_beneficiario(request, id_participante):


    return render(request, '04_participante/consultar_dados_beneficiario.html', locals())