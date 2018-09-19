from django.db import models

from django.contrib.auth.models import User
from core.models import Regiao, Estado, Municipio, Status_Geral
from participante.models import Participante


class Equipe_trabalho(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True)
    nome = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nome da Equipe de Trabalho")
    descricao = models.TextField(max_length=2000, blank=True, null=True, verbose_name=u'Descrição da Equipe de Trabalho')

    def __str__(self):
        return self.nome


class Unidade_gestora(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True)
    nome = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nome da Unidade Gestora")
    descricao = models.TextField(max_length=2000, blank=True, null=True, verbose_name=u'Descrição da Unidade Gestora')
    ug_municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.PROTECT, verbose_name=u'Municipio da Unidade Gestora')

    def __str__(self):
        return self.nome


class Tipo_atividade(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True)
    categoria = models.CharField(max_length=200, null=True, blank=True, verbose_name="Categoria da Atividade de Trabalho")
    nome = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nome do Tipo da Atividade de Trabalho")
    descricao = models.TextField(max_length=2000, blank=True, null=True, verbose_name=u'Descrição do Tipo da Atividade de Trabalho')

    def __str__(self):
        return self.nome


class Trabalho_campo(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True)

    nome = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nome do Tipo da Atividade de Trabalho")
    descricao = models.TextField(max_length=2000, blank=True, null=True, verbose_name=u'Descrição do Tipo da Atividade de Trabalho')

    at_equipe_trabalho = models.ForeignKey(Equipe_trabalho, null=True, blank=True, on_delete=models.PROTECT, verbose_name=u'Equipe de Trabalho da Atividade')
    at_unidade_gestora = models.ForeignKey(Unidade_gestora, null=True, blank=True, on_delete=models.PROTECT, verbose_name=u'Unidade Gestora da Atividade')
    at_tipo_atividade = models.ForeignKey(Tipo_atividade, null=True, blank=True, on_delete=models.PROTECT, verbose_name=u'Tipo da Atividade de Trabalho')
    user_created = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    at_municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.PROTECT, verbose_name=u'Municipio da Atividade')
    at_status = models.ForeignKey(Status_Geral, null=True, blank=True, on_delete=models.PROTECT)
    dt_closed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Ocorrencia(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True)

    num_protocolo = models.CharField(max_length=200, null=True, blank=True, verbose_name="Numero do protocolo da ocorrência")
    dt_solicitacao = models.DateTimeField(null=True, blank=True)
    nome_solicitante = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nome do Solicitante da ocorrência")
    tel_solicitante = models.CharField(max_length=25, null=True, blank=True, verbose_name="Telefone do Solicitante")
    email_solicitante = models.CharField(max_length=150, null=True, blank=True, verbose_name="E-mail do Solicitante")

    beneficiario_participante = models.ForeignKey(Participante, null=True, blank=True, on_delete=models.PROTECT,
                                                  verbose_name=u'Beneficiário da ocorrencia')

    questionamento = models.TextField(max_length=2000, blank=True, null=True, verbose_name=u'Questionamento da ocorrência')
    user_atendente = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, verbose_name=u'Usuario atendente')
    dt_solucao_ocorrencia = models.DateTimeField(null=True, blank=True)
    user_atendente = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, verbose_name=u'Municipio da ocorrência')
    equipe_responsavel = models.ForeignKey(Equipe_trabalho, null=True, blank=True, on_delete=models.PROTECT, verbose_name=u'Equipe responsável pela ocorrência')
    municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.PROTECT, verbose_name=u'Município da ocorrência')

    status = models.ForeignKey(Status_Geral, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.num_protocolo


class Tarefa_correncia(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, null=True)

    ocorrencia = models.ForeignKey(Ocorrencia, null=True, blank=True, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=200, null=True, blank=True, verbose_name="Titulo da solução")
    solucao = models.TextField(max_length=2000, blank=True, null=True, verbose_name=u'Solução adotada')
    dt_solucao = models.DateTimeField(null=True, blank=True)

    equipe_responsavel_solucao = models.ForeignKey(Equipe_trabalho, null=True, blank=True, on_delete=models.PROTECT,
                                                   verbose_name=u'Equipe responsável pela solução da ocorrência')

    def __str__(self):
        return titulo
