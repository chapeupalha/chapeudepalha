from django.db import models
from random import randint
import os
import datetime

from django.contrib.auth.models import User


class EstadoCivil(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome do estado civil")


class TipoDocumentoEmpregador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome do tipo de documento do empregador")


class GrauEscolaridade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome do grau da escolaridade")


class TurnoEscolar(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome do Turno")


class Deficiencia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome da Deficiência")


class Raca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome da raça do participante")


# class DadosParticipante(models.Model):
#     usuario = models.ForeignKey(User, null=False, blank=True, verbose_name="ID do usuário participante")
#     municipio = models.ForeignKey(fazer_ainda, null=True, blank=True, verbose_name="Municipio do participante")
#     nis = models.CharField(max_length=15, null=False, verbose_name="Número do NIS")
#     nis_atual = models.CharField(max_length=15, null=True, verbose_name="Número do NIS atualizado na CEF")
#     cpf = models.CharField(max_length=11, null=False, verbose_name="Número do CPF")
#     rg = models.CharField(max_length=20, null=True, verbose_name="Número do RG")
#     rg_orgao_exp = models.CharField(max_length=20, null=True, verbose_name="Órgão expedidor do RG")
#     rg_uf = models.CharField(max_length=2, null=True, verbose_name="UF do RG")
#     dt_nascimento = models.DateTimeField(verbose_name="Data de nascimento do participante")
#     sexo = models.CharField(max_length=1, null=False, verbose_name="Sexo do participante")
#     estado_civil = models.ForeignKey(EstadoCivil, verbose_name="Estado civvil do participante")
#     municipio_naturalidade = models.CharField(null=True, verbose_name="Naturalidade do participante")
#     uf_naturalidade = models.CharField(null=True, verbose_name="UF da naturalidade do participante")
#     titulo_eleitor = models.CharField(null=True, verbose_name="Titulo de eleitor do participante")
#     ctps = models.CharField(null=True, verbose_name="CTPS do participante")
#     ctps_serie = models.CharField(null=True, verbose_name="Série da CTPS do participante")
#     ctps_uf = models.CharField(null=True, verbose_name="UF da CTPS do participante")
#     tipo_documento_empregador = models.ForeignKey(TipoDocumentoEmpregador, verbose_name="Tipo de documento do empregador")
#     cnpj_ultimo_empregador = models.CharField(null=True, verbose_name="Número do documento do empregador")
#     nome_empresa = models.CharField(null=True, verbose_name="Nome do empregador")
#     funcao = models.CharField(null=True, verbose_name="Função realizada pelo participante")
#     dt_entrada = models.DateTimeField(null=True, verbose_name="Data inicial de contrato de trabalho")
#     dt_saida = models.DateTimeField(null=True, verbose_name="Data final de contrato de trabalho")
#     nome_pai = models.CharField(null=True, verbose_name="Nome do Pai")
#     nome_mae = models.CharField(null=False, verbose_name="Nome da Mãe")
#     qtd_filhos_0_6_meses = models.IntegerField(null=True, verbose_name="Quantidade de filhos entre 0 a 6 meses")
#     qtd_filhos_7_meses_3_anos = models.IntegerField(null=True, verbose_name="Quantidade de filhos entre 7 meses a 3 anos")
#     qtd_filhos_4_7_anos = models.IntegerField(null=True, verbose_name="Quantidade de filhos entre 4 a 7 anos")
#     qtd_filhos_8_12_anos = models.IntegerField(null=True, verbose_name="Quantidade de filhos entre 8 a 12 anos")
#     qtd_filhos_13_17_anos = models.IntegerField(null=True, verbose_name="Quantidade de filhos entre 13 a 17 anos")
#     qtd_filhos_18_29_anos = models.IntegerField(null=True, verbose_name="Quantidade de filhos entre 18 a 29 anos")
#     gestante_familia = models.BooleanField(null=True, verbose_name="Existe gestante na familia")
#     alfabetizado = models.BooleanField(null=True, verbose_name="participante é alfabetizado")
#     grau_escolaridade = models.ForeignKey(GrauEscolaridade, verbose_name="Grau de escolaridade do participante")
#     endereco = models.CharField(null=True, verbose_name="Endereco do participante")
#     numero = models.CharField(null=True, verbose_name="Número do endereco do participante")
#     complemento = models.CharField(null=True, verbose_name="Complemento do endereco do participante")
#     bairro = models.CharField(null=True, verbose_name="Complemento do endereco do participante")
#     cep = models.CharField(null=True, verbose_name="cep do participante")
#     celular = models.CharField(null=True, verbose_name="Número de celular do participante")
#     fone = models.CharField(null=True, verbose_name="Número de telefone do participante")
#     renda_mensal = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name="Renda mensal do participante")
#     qtd_pessoas_casa = models.IntegerField(null=True, verbose_name="Quantidade de pessoas que moram na casa")
#     qtd_pessoas_contribuem_renda = models.IntegerField(null=True, verbose_name="Quantidade de pessoas que contribuem com a renda")
#     beneficiario_indicado = models.BooleanField(null=True, verbose_name="Participante será o indicado")
#     apresentou_nis = models.BooleanField(null=True, verbose_name="Apresentou copia do ")
#     apresentou_contrato_trabalho = models.BooleanField(null=True, verbose_name="Apresentou copia do contrato de trabalho")
#     apresentou_ctps = models.BooleanField(null=True, verbose_name="Apresentou copia do ctps")
#     apresentou_cpf = models.BooleanField(null=True, verbose_name="Apresentou copia do cpf")
#     apresentou_rg = models.BooleanField(null=True, verbose_name="Apresentou copia do rg")
#     apresentou_endereco = models.BooleanField(null=True, verbose_name="Apresentou copia do endereco")
#     apresentou_listagem_desligado = models.BooleanField(null=True, verbose_name="Apresentou copia da listagem de desligados")
#     estudando = models.BooleanField(null=True, verbose_name="Está estudando")
#     turno_atividade_escolar = models.ForeignKey(TurnoEscolar, verbose_name="Turno em que esta estudando atualmente")
#     portador_deficiencia = models.ForeignKey(Deficiencia, verbose_name="Portador de deficiencia")
#     raca = models.ForeignKey(Raca, verbose_name="Raça do participante")
#     status_participante = models.ForeignKey(fazer_ainda, verbose_name="Status do participante")
#     dt_cadastro = models.DateTimeField(verbose_name="Data de cadastro")
#     dt_alteracao = models.DateTimeField(verbose_name="Data da alteracao")
#     usuario_updated = models.ForeignKey(User, verbose_name="Usuário que realizou o cadastro")

