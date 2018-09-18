from django.db import models
from random import randint
import os
import datetime

from .utils import update_filename
from django.contrib.auth.models import User
from core.models import Regiao, Estado, Municipio, Status_Geral
from core.choices import CHOICES_SEXO, CHOICES_UF, CHOICES_SIM_NAO


class EstadoCivil(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome do estado civil")

    def __str__(self):
        return self.nome


class TipoDocumentoEmpregador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome do tipo de documento do empregador")

    def __str__(self):
        return self.nome


class GrauEscolaridade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome do grau da escolaridade")

    def __str__(self):
        return self.nome


class TurnoEscolar(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome do Turno")

    def __str__(self):
        return self.nome


class Deficiencia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome da Deficiência")

    def __str__(self):
        return self.nome


class Raca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Nome da raça do participante")

    def __str__(self):
        return self.nome


class TipoCopiaDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, blank=True, verbose_name="Tipo da cópia do documento")
    nome_bd = models.CharField(max_length=500, blank=True, verbose_name="Nome do documento para utilizar no sistema")

    def __str__(self):
        return self.nome


class Participante(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    dt_cadastro = models.DateTimeField(auto_now_add=True, null=True)
    dt_alteracao = models.DateTimeField(auto_now_add=True, null=True)
    usuario_updated = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='usuario_update')

    nis_pis = models.CharField(max_length=15, null=True, blank=True, verbose_name="Número do NIS")
    nome_completo = models.CharField(max_length=150, null=True, blank=True, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, null=True, blank=True, verbose_name="Número do CPF")
    rg = models.CharField(max_length=20, null=True, blank=True, verbose_name="Número do RG")
    rg_orgao_exp = models.CharField(max_length=20, null=True, blank=True, verbose_name="Órgão expedidor do RG")
    rg_uf = models.CharField(max_length=20, null=True, blank=True, choices=CHOICES_UF, verbose_name="UF do RG")

    nome_pai = models.CharField(max_length=150, null=True, blank=True, verbose_name="Nome do Pai")
    nome_mae = models.CharField(max_length=150, null=True, blank=True, verbose_name="Nome da Mãe")
    dt_nascimento = models.DateTimeField(null=True, blank=True, verbose_name="Data de nascimento do participante")
    sexo = models.CharField(max_length=20, null=True, blank=True, choices=CHOICES_SEXO, verbose_name=u"Sexo do participante")
    estado_civil = models.ForeignKey(EstadoCivil, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Estado civil do participante")
    municipio_naturalidade = models.ForeignKey(Municipio, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Naturalidade do participante")
    titulo_eleitor = models.CharField(max_length=50, null=True, blank=True, verbose_name="Titulo de eleitor do participante")
    ctps = models.CharField(max_length=100, null=True, blank=False, verbose_name="Carteira de trabalho Nº")
    ctps_serie = models.CharField(max_length=100, null=True, blank=False, verbose_name="Série da carteira de trabalho")
    ctps_uf = models.CharField(max_length=20, null=True, blank=True, choices=CHOICES_UF, verbose_name="UF da carteira de trabalho")

    tipo_documento_empregador = models.ForeignKey(TipoDocumentoEmpregador, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Tipo de documento do empregador")
    cnpj_ultimo_empregador = models.CharField(max_length=25, null=True, blank=True, verbose_name="Número do documento do último empregador")
    nome_empresa = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome da empresa (Razão Social)")
    funcao = models.CharField(max_length=100, null=True, blank=True, verbose_name="Função realizada pelo participante")
    dt_entrada = models.DateTimeField(null=True, blank=True, verbose_name="Data inicial de contrato de trabalho")
    dt_saida = models.DateTimeField(null=True, blank=True, verbose_name="Data final de contrato de trabalho")

    qtd_filhos_0_m_6_m = models.IntegerField(null=True, blank=True, verbose_name="Quantidade de filhos entre 0 a 6 meses")
    qtd_filhos_7_m_3_a = models.IntegerField(null=True, blank=True, verbose_name="Quantidade de filhos entre 7 meses a 3 anos")
    qtd_filhos_4_a_7_a = models.IntegerField(null=True, blank=True, verbose_name="Quantidade de filhos entre 4 a 7 anos")
    qtd_filhos_8_a_12_a = models.IntegerField(null=True, blank=True, verbose_name="Quantidade de filhos entre 8 a 12 anos")
    qtd_filhos_13_a_17_a = models.IntegerField(null=True, blank=True, verbose_name="Quantidade de filhos entre 13 a 17 anos")
    qtd_filhos_18_a_29_a = models.IntegerField(null=True, blank=True, verbose_name="Quantidade de filhos entre 18 a 29 anos")
    gestante_familia = models.IntegerField(null=True, blank=True, choices=CHOICES_SIM_NAO, verbose_name="Existe gestante na familia")
    alfabetizado = models.IntegerField(null=True, blank=True, choices=CHOICES_SIM_NAO, verbose_name="participante é alfabetizado")
    estudando = models.IntegerField(null=True, blank=True, choices=CHOICES_SIM_NAO, verbose_name="Está estudando")
    turno_atividade_escolar = models.ForeignKey(TurnoEscolar, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Turno em que esta estudando atualmente")
    grau_escolaridade = models.ForeignKey(GrauEscolaridade, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Grau de escolaridade do participante")
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Raça do participante")
    portador_deficiencia = models.ForeignKey(Deficiencia, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Portador de deficiencia")
    logradouro = models.CharField(max_length=150, null=True, blank=True, verbose_name="Logradouro")
    numero = models.CharField(max_length=10, null=True, blank=True, verbose_name="Número do endereco do participante")
    complemento = models.CharField(max_length=150, null=True, blank=True, verbose_name="Complemento do endereco do participante")
    municipio_participante = models.ForeignKey(Municipio, on_delete=models.PROTECT, null=True, blank=True, related_name='municipio_participante', verbose_name="Municipio do participante")
    cep = models.CharField(max_length=50, null=True, blank=True, verbose_name="cep do participante")
    fone = models.CharField(max_length=50, null=True, blank=True, verbose_name="Número de telefone do participante")
    celular = models.CharField(max_length=50, null=True, blank=True, verbose_name="Número de celular do participante")

    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Renda mensal do participante")
    qtd_pessoas_casa = models.IntegerField(null=True, blank=True, verbose_name="Quantidade de pessoas que moram na casa")
    qtd_pessoas_contribuem_renda = models.IntegerField(null=True, blank=True, verbose_name="Quantidade de pessoas que contribuem com a renda")
    # beneficiario_indicado = models.BooleanField(null=True, verbose_name="Participante será o indicado")
    # verificacao_listagem_desligado = models.BooleanField(null=True, verbose_name="Apresentou copia da listagem de desligados")

    verificacao_nis = models.BooleanField(default=False, verbose_name="Apresentou copia do NIS")
    verificacao_contrato_trabalho = models.BooleanField(default=False, verbose_name="Apresentou copia do contrato de trabalho")
    verificacao_ctps = models.BooleanField(default=False, verbose_name="Apresentou copia do ctps")
    verificacao_cpf = models.BooleanField(default=False, verbose_name="Apresentou copia do cpf")
    verificacao_rg = models.BooleanField(default=False, verbose_name="Apresentou copia do rg")
    verificacao_endereco = models.BooleanField(default=False, verbose_name="Apresentou copia do endereco")

    verificacao_dados_participante = models.BooleanField(default=False, verbose_name="Alguma pendência nos dados do participante")
    verificacao_representante_legal = models.BooleanField(default=False, verbose_name="Alguma pendência nos dados do representante legal")
    verificacao_documentacao = models.BooleanField(default=False, verbose_name="Alguma pendência na entrega da documentacao")

    possui_representante_legal = models.BooleanField(default=True, choices=CHOICES_SIM_NAO, verbose_name="Possui representante legal")
    representante_legal_nis_pis = models.CharField(max_length=50, null=True, blank=True, verbose_name="NIS/PIS do representante legal")
    representante_legal_nome = models.CharField(max_length=150, null=True, blank=True, verbose_name="Nome do representante legal")
    representante_legal_cpf = models.CharField(max_length=20, null=True, blank=True, verbose_name="CPF do representante legal")
    representante_legal_dt_nascimento = models.DateTimeField(null=True, blank=True, verbose_name="Data de nascimento do representante legal")

    status = models.ForeignKey(Status_Geral, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Status do participante")

    def __str__(self):
        return self.nome_completo


class DocumentosParticipante(models.Model):
    documento = models.FileField(max_length=1000, upload_to=update_filename, null=True, blank=True, verbose_name=u"BUSCAR ARQUIVO NO COMPUTADOR")
    participante = models.ForeignKey(Participante, null=True, blank=True, on_delete=models.CASCADE)
    tipo_documento = models.ForeignKey(TipoCopiaDocumento, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Tipo do documento")
    dt_cadastro = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.desc_documento
