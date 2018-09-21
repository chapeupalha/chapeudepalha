from django.urls import path

from .views import *

urlpatterns = [
    path('curso/', home_curso, name='home_curso'),
    path('curso/cadastro', curso_cadastro, name='curso_cadastro'),
    path('curso/lista', curso_lista, name='curso_lista'),
    path('curso/alterar', curso_alterar, name='curso_alterar'),
    path('curso/<int:id_curso>/atualizar', curso_atualizar, name='curso_atualizar'),
    path('curso/<int:id_curso>/visualizar', curso_visualizar, name='curso_visualizar'),

    path('local/', home_local, name='home_local'),
    path('local/cadastro', local_cadastro, name='local_cadastro'),
    path('local/consulta', local_consulta, name='local_consulta'),
    path('local/consulta/<int:id_local>/atualizar', local_atualizar, name='local_atualizar'),
    path('local/consulta/<int:id_local>/visualizar', local_visualizar, name='local_visualizar'),

    path('local/secretaria/cadastro', secretaria_cadastro, name='secretaria_cadastro'),
    path('local/secretaria/consulta', secretaria_consulta, name='secretaria_consulta'),
    path('local/secretaria/<int:id_secretaria>/atualizar', secretaria_atualizar, name='secretaria_atualizar'),
    path('local/secretaria/<int:id_secretaria>/visualizar', secretaria_visualizar, name='secretaria_visualizar'),

    path('turma/', home_turma, name='home_turma'),
    path('turma/cadastrar_turma', cadastrar_turma, name='cadastrar_turma'),
    path('turma/listar', listar_turma, name='listar_turma'),
    path('turma/<int:id_turma>/atualizar', turma_atualizar, name='turma_atualizar'),
    path('turma/<int:id_turma>/visualizar', turma_visualizar, name='turma_visualizar'),
    path('turma/<int:id_turma>/inserir_aluno', turma_inserir_aluno, name='turma_inserir_aluno'),
    path('turma/<int:id_turma>/inserir_aluno_turma/<int:id_participante>/aluno', cadastrar_aluno_turma, name='cadastrar_aluno_turma'),
    path('turma/<int:id_turma>/remover_aluno_turma/<int:id_participante>/aluno', remover_aluno_turma, name='remover_aluno_turma'),
    path('turma/<int:id_turma>/finalizar_turma', finalizar_turma, name='finalizar_turma'),

    path('frequencia/', frequencia_home, name='frequencia_home'),
    path('frequencia/<int:id_curso>/curso', frequencia_curso_turma, name='frequencia_curso_turma'),
    path('frequencia/<int:id_curso>/curso/<int:id_turma>/turma/', cadastro_frequencia_aluno, name='cadastro_frequencia_aluno'),
]
