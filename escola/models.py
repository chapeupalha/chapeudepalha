from django.db import models

from core.models import Status_Geral, Municipio
from participante.models import Participante
from core.choices import CHOICES_TURNO


class Secretaria(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name='Nome da secretaria')
    sigla = models.CharField(max_length=20, blank=True, verbose_name='Sigla da secretaria')
    nome_responsavel = models.CharField(max_length=500, blank=True, verbose_name='Nome do responsável')
    tel_responsavel = models.CharField(max_length=500, blank=True, verbose_name='Tel do responsável')
    email_responsavel = models.CharField(max_length=500, blank=True, verbose_name='E-mail do responsável')
    status = models.ForeignKey(Status_Geral, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Local(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name='Nome do local')
    endereco = models.CharField(max_length=500, blank=True, verbose_name='Logradouro')
    end_numero = models.IntegerField(null=True, blank=True, verbose_name='Numero')
    complemento = models.CharField(max_length=500, blank=True, verbose_name='Complemento')
    cep = models.CharField(max_length=500, blank=True, verbose_name='CEP')
    nome_responsavel = models.CharField(max_length=500, blank=True, verbose_name='Nome do responsável')
    tel_responsavel = models.CharField(max_length=500, blank=True, verbose_name='Tel do responsável')
    email_responsavel = models.CharField(max_length=500, blank=True, verbose_name='E-mail do responsável')
    secretaria = models.BooleanField(default=False, verbose_name='Local disponibilizado para secretaria')

    municipio_local = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Municipio')
    status = models.ForeignKey(Status_Geral, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name='Nome do curso')
    descricao = models.TextField(max_length=2000, blank=True, null=True, verbose_name=u'Descrição do curso')
    qtd_horas = models.IntegerField(null=True, blank=True, verbose_name='Quantidade de horas')
    dt_inicio = models.DateTimeField(null=True, blank=True, verbose_name='Data de inicio')
    dt_final = models.DateTimeField(null=True, blank=True, verbose_name='Data Final')

    secretaria_curso = models.ForeignKey(Secretaria, null=True, blank=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status_Geral, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name='Nome da turma')
    qtd_aluno_min = models.IntegerField(null=True, blank=True, verbose_name='Quantidade maxima de alunos')
    qtd_aluno_max = models.IntegerField(null=True, blank=True, verbose_name='Quantidade minima de alunos')
    turno = models.CharField(max_length=20, null=True, blank=True, choices=CHOICES_TURNO, default='Matutino', verbose_name=u"Turno escolar")
    observacoes = models.TextField(max_length=2000, blank=True, null=True, verbose_name=u'Observações')
    dia_seg = models.BooleanField(default=False, verbose_name='Segunda-Feira')
    dia_ter = models.BooleanField(default=False, verbose_name='Terça-Feira')
    dia_qua = models.BooleanField(default=False, verbose_name='Quarta-Feira')
    dia_qui = models.BooleanField(default=False, verbose_name='Quinta-Feira')
    dia_sex = models.BooleanField(default=False, verbose_name='Sexta-Feira')
    dia_sab = models.BooleanField(default=False, verbose_name='Sábado')
    dia_dom = models.BooleanField(default=False, verbose_name='Domingo')

    curso_turma = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    local_turma = models.ForeignKey(Local, null=True, blank=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status_Geral, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class aluno_participa_turma(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    turma = models.ForeignKey(Turma, null=True, blank=True, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Participante, null=True, blank=True, on_delete=models.CASCADE)


class Aula_frequencia(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dia_semana = models.CharField(max_length=500, blank=True)
    data_aula = models.DateTimeField(null=True, blank=True)

    turma = models.ForeignKey(Turma, null=True, blank=True, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Participante, null=True, blank=True, on_delete=models.CASCADE)
