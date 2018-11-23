from django.shortcuts import render, redirect
import datetime

from escola.forms import cadastro_secretaria_form, cadastro_local_form, cadastro_curso_form, cadastro_turma_form

from escola.models import Secretaria, Local, Curso, Turma, aluno_participa_turma, Aula_frequencia
from core.models import Status_Geral
from participante.models import Participante


def home_curso(request):
    active_menu = 'escola'

    all_cursos = Curso.objects.all()

    return render(request, '07_escola/curso/home.html', locals())


def curso_cadastro(request):
    active_menu = 'escola'
    action_form = 'add'
    curso_form = cadastro_curso_form(request.POST or None)

    if request.method == 'POST':
        if curso_form.is_valid():
            status_local = Status_Geral.objects.get(item='CURSO', chave='CADASTRO_NOVO_CURSO')

            formcurso_obj = curso_form.save(commit=False)
            formcurso_obj.status = status_local

            formcurso_obj.save()
            return redirect('/capacitacao/curso/lista')

    return render(request, '07_escola/curso/cadastro.html', locals())


def curso_lista(request):
    active_menu = 'escola'
    all_cursos = Curso.objects.all()

    return render(request, '07_escola/curso/curso_lista.html', locals())


def curso_atualizar(request, id_curso):
    active_menu = 'escola'
    action_form = 'att'
    obj_curso = Curso.objects.get(id=id_curso)
    curso_form = cadastro_curso_form(request.POST or None, instance=obj_curso)

    if request.method == 'POST':
        if curso_form.is_valid():
            status_local = Status_Geral.objects.get(item='CURSO', chave='CADASTRO_NOVO_CURSO')

            formcurso_obj = curso_form.save(commit=False)
            formcurso_obj.status = status_local

            formcurso_obj.save()
            return redirect('/capacitacao/curso/lista')

    return render(request, '07_escola/curso/cadastro.html', locals())


def curso_visualizar(request, id_curso):
    active_menu = 'escola'
    obj_curso = Curso.objects.get(id=id_curso)

    if request.method == 'POST':
        if request.POST.get('disable_curso') == 'true':
            status_curso = Status_Geral.objects.get(item='CURSO', chave='CURSO_FINALIZADO')
            Curso.objects.filter(id=id_curso).update(status=status_curso)
            return redirect('/capacitacao/curso/lista')

        elif request.POST.get('disable_curso') == 'false':
            status_curso = Status_Geral.objects.get(item='CURSO', chave='CADASTRO_NOVO_CURSO')
            Curso.objects.filter(id=id_curso).update(status=status_curso)
            return redirect('/capacitacao/curso/lista')

    return render(request, '07_escola/curso/visualizar.html', locals())


def curso_alterar(request):
    active_menu = 'escola'
    all_cursos = Curso.objects.all()

    return render(request, '07_escola/curso/curso_lista_alterar.html', locals())


def home_local(request):
    active_menu = 'escola'


    return render(request, '07_escola/local/home.html', locals())


def local_cadastro(request):
    active_menu = 'escola'
    action_form = 'add'
    local_form = cadastro_local_form(request.POST or None)

    if request.method == 'POST':
        if local_form.is_valid():
            status_local = Status_Geral.objects.get(item='LOCAL_ESCOLA', chave='CADASTRO_LOCAL')

            local_obj = local_form.save(commit=False)
            local_obj.status = status_local

            local_obj.save()
            return redirect('/capacitacao/local/')

    return render(request, '07_escola/local/local_cadastro.html', locals())


def local_consulta(request):
    active_menu = 'escola'
    local_escola = Local.objects.all()


    return render(request, '07_escola/local/local_consulta.html', locals())


def local_atualizar(request, id_local):
    active_menu = 'escola'
    action_form = 'att'
    obj_local = Local.objects.get(id=id_local)
    local_form = cadastro_local_form(request.POST or None, instance=obj_local)

    if request.method == 'POST':
        if local_form.is_valid():
            status_local = Status_Geral.objects.get(item='LOCAL_ESCOLA', chave='CADASTRO_LOCAL')

            local_obj = local_form.save(commit=False)
            local_obj.status = status_local

            local_obj.save()
            return redirect('/capacitacao/local/consulta')

    return render(request, '07_escola/local/local_cadastro.html', locals())


def local_visualizar(request, id_local):
    active_menu = 'escola'
    local_obj = Local.objects.get(id=id_local)

    if request.method == 'POST':
        if request.POST.get('disable_local') == 'true':
            status_local = Status_Geral.objects.get(item='LOCAL_ESCOLA', chave='DESABILITAR_LOCAL')
            Local.objects.filter(id=id_local).update(status=status_local)
            return redirect('/capacitacao/local/consulta')

        elif request.POST.get('disable_local') == 'false':
            status_local = Status_Geral.objects.get(item='LOCAL_ESCOLA', chave='CADASTRO_LOCAL')
            Local.objects.filter(id=id_local).update(status=status_local)
            return redirect('/capacitacao/local/consulta')

    return render(request, '07_escola/local/local_visualizar.html', locals())


def secretaria_cadastro(request):
    active_menu = 'escola'
    action_form = 'add'
    sec_form = cadastro_secretaria_form(request.POST or None)

    if request.method == 'POST':
        if sec_form.is_valid():
            status_secretaria = Status_Geral.objects.get(item='SECRETARIA', chave='CADASTRO_SECRETARIA')

            sec_obj = sec_form.save(commit=False)
            sec_obj.status = status_secretaria

            sec_obj.save()
            return redirect('/capacitacao/local/')

    return render(request, '07_escola/local/secretaria_cadastro.html', locals())


def secretaria_consulta(request):
    active_menu = 'escola'

    all_sec = Secretaria.objects.all()

    return render(request, '07_escola/local/secretaria_consulta.html', locals())


def secretaria_atualizar(request, id_secretaria):
    active_menu = 'escola'
    action_form = 'att'
    obj_sec = Secretaria.objects.get(id=id_secretaria)
    sec_form = cadastro_secretaria_form(request.POST or None, instance=obj_sec)

    if request.method == 'POST':
        if sec_form.is_valid():
            status_secretaria = Status_Geral.objects.get(item='SECRETARIA', chave='CADASTRO_SECRETARIA')

            sec_obj = sec_form.save(commit=False)
            sec_obj.status = status_secretaria

            sec_obj.save()
            return redirect('/capacitacao/local/secretaria/consulta')

    return render(request, '07_escola/local/secretaria_cadastro.html', locals())


def secretaria_visualizar(request, id_secretaria):
    active_menu = 'escola'
    obj_sec = Secretaria.objects.get(id=id_secretaria)

    if request.method == 'POST':
        if request.POST.get('disable_secretaria') == 'true':
            status_secretaria = Status_Geral.objects.get(item='SECRETARIA', chave='DESABILITAR_SECRETARIA')
            Secretaria.objects.filter(id=id_secretaria).update(status=status_secretaria)
            return redirect('/capacitacao/local/secretaria/consulta')

        elif request.POST.get('disable_secretaria') == 'false':
            status_secretaria = Status_Geral.objects.get(item='SECRETARIA', chave='CADASTRO_SECRETARIA')
            Secretaria.objects.filter(id=id_secretaria).update(status=status_secretaria)
            return redirect('/capacitacao/local/secretaria/consulta')

    return render(request, '07_escola/local/secretaria_visualizar.html', locals())


def home_turma(request):
    active_menu = 'escola'


    return render(request, '07_escola/turma/home.html', locals())


def cadastrar_turma(request):
    active_menu = 'escola'
    action_form = 'add'
    turma_form = cadastro_turma_form(request.POST or None)

    if request.method == 'POST':
        if turma_form.is_valid():
            status_turma = Status_Geral.objects.get(item='TURMA', chave='CADASTRO_TURMA')

            form_turma_obj = turma_form.save(commit=False)
            form_turma_obj.status = status_turma

            form_turma_obj.save()
            return redirect('/capacitacao/turma/listar')

    return render(request, '07_escola/turma/cadastrar_turma.html', locals())


def listar_turma(request):
    active_menu = 'escola'

    all_turmas = Turma.objects.all()


    return render(request, '07_escola/turma/listar_turma.html', locals())


def turma_atualizar(request, id_turma):
    active_menu = 'escola'
    action_form = 'att'
    obj_turmas = Turma.objects.get(id=id_turma)
    turma_form = cadastro_turma_form(request.POST or None, instance=obj_turmas)

    if request.method == 'POST':
        if turma_form.is_valid():
            status_turma = Status_Geral.objects.get(item='TURMA', chave='CADASTRO_TURMA')

            form_turma_obj = turma_form.save(commit=False)
            form_turma_obj.status = status_turma

            form_turma_obj.save()
            return redirect('/capacitacao/turma/listar')

    return render(request, '07_escola/turma/cadastrar_turma.html', locals())


def turma_visualizar(request, id_turma):
    active_menu = 'escola'
    action_form = 'att'
    obj_turmas = Turma.objects.get(id=id_turma)
    turma_form = cadastro_turma_form(request.POST or None, instance=obj_turmas)

    if request.method == 'POST':
        if turma_form.is_valid():
            status_turma = Status_Geral.objects.get(item='TURMA', chave='CADASTRO_TURMA')

            form_turma_obj = turma_form.save(commit=False)
            form_turma_obj.status = status_turma

            form_turma_obj.save()
            return redirect('/capacitacao/turma/listar')

    return render(request, '07_escola/turma/turma_visualizar.html', locals())


def turma_inserir_aluno(request, id_turma):
    active_menu = 'escola'
    turma_completa = False
    obj_turmas = Turma.objects.get(id=id_turma)
    all_alunos_turma = aluno_participa_turma.objects.filter(turma=obj_turmas).order_by('aluno')

    remove_aluno = aluno_participa_turma.objects.filter(turma=obj_turmas).values_list('aluno')
    all_participantes = Participante.objects.filter(status_id=10010300).exclude(id__in=remove_aluno).order_by('nome_completo')

    capacidade_turma = aluno_participa_turma.objects.filter(turma=obj_turmas).count()
    quantidade_atual = obj_turmas.qtd_aluno_max
    if capacidade_turma >= quantidade_atual or capacidade_turma == quantidade_atual:
        turma_completa = True

    return render(request, '07_escola/turma/turma_inserir_aluno.html', locals())


def cadastrar_aluno_turma(request, id_turma, id_participante):
    active_menu = 'escola'
    obj_turmas = Turma.objects.get(id=id_turma)
    obj_participante = Participante.objects.get(id=id_participante)

    capacidade_turma = aluno_participa_turma.objects.filter(turma=obj_turmas).count()
    quantidade_atual = obj_turmas.qtd_aluno_max

    if capacidade_turma < quantidade_atual:
        lista_turma = aluno_participa_turma(
            turma=obj_turmas,
            aluno=obj_participante,
        )
        lista_turma.save()
    else:
        turma_completa = True

    return redirect('/capacitacao/turma/%s/inserir_aluno' % (id_turma,))


def remover_aluno_turma(request, id_turma, id_participante):
    active_menu = 'escola'
    obj_turma = Turma.objects.get(id=id_turma)
    obj_participante = Participante.objects.get(id=id_participante)

    aluno_participa_turma.objects.filter(turma=obj_turma, aluno=obj_participante).delete()

    return redirect('/capacitacao/turma/%s/inserir_aluno' % (id_turma,))


def finalizar_turma(request, id_turma):
    active_menu = 'escola'
    status_turma = Status_Geral.objects.get(item='TURMA', chave='ALUNOS_CADASTRADO_TURMA')
    Turma.objects.filter(id=id_turma).update(status=status_turma)

    return redirect('/capacitacao/turma/listar')


def frequencia_home(request):
    active_menu = 'frequencia'
    all_curso = Curso.objects.all()
    return render(request, '07_escola/frequencia/home.html', locals())


def frequencia_curso_turma(request, id_curso):
    active_menu = 'frequencia'
    obj_curso = Curso.objects.get(id=id_curso)

    turma_by_curso = Turma.objects.filter(curso_turma=obj_curso)

    # turma_by_curso = aluno_participa_turma.objects.filter(curso=obj_curso)

    return render(request, '07_escola/frequencia/curso_turma.html', locals())


def cadastro_frequencia_aluno(request, id_curso, id_turma):
    active_menu = 'frequencia'
    obj_curso = Curso.objects.get(id=id_curso)
    obj_turma = Turma.objects.get(id=id_turma)

    chamada_completa = Aula_frequencia.objects.filter(turma=obj_turma)

    if request.method == 'POST':
        beneficiario = Participante.objects.get(card_id=request.POST.get('card-frequencia'))
        now = datetime.datetime.now()
        diaSemana = None
        if datetime.datetime.now().isoweekday() == 1:
            diaSemana = 'Segunda-feira'
        elif datetime.datetime.now().isoweekday() == 2:
            diaSemana = 'Terça-feira'
        elif datetime.datetime.now().isoweekday() == 3:
            diaSemana = 'Quarta-feira'
        elif datetime.datetime.now().isoweekday() == 4:
            diaSemana = 'Quinta-feira'
        elif datetime.datetime.now().isoweekday() == 5:
            diaSemana = 'Sexta-feira'
        elif datetime.datetime.now().isoweekday() == 6:
            diaSemana = 'Sábado'
        elif datetime.datetime.now().isoweekday() == 7:
            diaSemana = 'Domingo'

        aluno_registrado = Aula_frequencia.objects.filter(turma=obj_turma, aluno=beneficiario, dia_semana=diaSemana).exists()
        aluno_participa_da_turma = aluno_participa_turma.objects.filter(turma=obj_turma, aluno=beneficiario).exists()

        if not aluno_registrado:
            if aluno_participa_da_turma:
                chamada = Aula_frequencia(
                    dia_semana=diaSemana,
                    data_aula=now,
                    turma=obj_turma,
                    aluno=beneficiario,
                )
                chamada.save()
        chamada_completa = Aula_frequencia.objects.filter(turma=obj_turma)
        return redirect('/capacitacao/frequencia/%s/curso/%s/turma/' % (id_curso, id_turma))

    return render(request, '07_escola/frequencia/cadastro_frequencia_aluno.html', locals())
