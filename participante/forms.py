# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from participante.models import Participante


class cadastro_participante(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_participante, self).__init__(*args, **kwargs)

    class Meta:
        model = Participante

        widgets = {
            'nome_completo' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o nome completo do beneficiário', 'required': True}),
            'cpf' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o CPF do beneficiário', 'required': True}),
        }

        fields = ('cpf', 'nome_completo', 'status', 'usuario',)


class cadastro_dados_participante(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_dados_participante, self).__init__(*args, **kwargs)

    class Meta:
        model = Participante

        widgets = {
            'nis_pis' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'NIS/PIS do beneficiário', 'required': True}),
            'cpf': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CPF do beneficiário', 'required': True}),
            'rg' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'RG do beneficiário', 'required': True}),
            'rg_orgao_exp' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Órgão expedidor do RG', 'required': True}),
            'rg_uf' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'UF do órgão expedidor', 'required': True}),
            'nome_completo': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome completo do beneficiário', 'required': True}),
            'nome_mae' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome da Mãe do beneficiário', 'required': True}),
            'nome_pai': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome de Pai do beneficiário', 'required': True}),
            'dt_nascimento' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Data de nascimento', 'required': True}),
            'sexo' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Sexo', 'required': True}),
            'titulo_eleitor' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Título de eleitor', 'required': True}),
            'ctps' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Número da carteira de trabalho(ctps)', 'required': True}),
            'ctps_serie' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Série da ctps', 'required': True}),
            'ctps_uf' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'UF da ctps', 'required': True}),
            'cnpj_ultimo_empregador' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CNPJ / CEI / CPF do último empregador', 'required': True}),
            'nome_empresa' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome da empresa (Razão social)', 'required': True}),
            'funcao' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Função', 'required': True}),
            'dt_entrada' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Data de entrada', 'required': True}),
            'dt_saida' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Data de saída', 'required': True}),
            'qtd_filhos_0_m_6_m' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 0 a 6 meses', 'required': True}),
            'qtd_filhos_7_m_3_a' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 7 meses a 3 anos', 'required': True}),
            'qtd_filhos_4_a_7_a' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 4 a 7 anos', 'required': True}),
            'qtd_filhos_8_a_12_a' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 8 a 12 anos', 'required': True}),
            'qtd_filhos_13_a_17_a' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 13 a 17 anos', 'required': True}),
            'qtd_filhos_18_a_29_a' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 18 a 29 anos', 'required': True}),
            'gestante_familia' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Há gestante na família', 'required': True}),
            'alfabetizado' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Alfabetizado?', 'required': True}),
            'estudando' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Está estudando?', 'required': True}),
            'logradouro' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Logradouro', 'required': True}),
            'numero' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Número', 'required': True}),
            'complemento' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Complemento', 'required': True}),
            'cep' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CEP', 'required': True}),
            'fone' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Telefone', 'required': True}),
            'celular' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Celular', 'required': True}),
            'renda_mensal' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Renda Mensal', 'required': True}),
            'qtd_pessoas_casa' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Quantidade de pessoas que moram na casa', 'required': True}),
            'qtd_pessoas_contribuem_renda' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Quantidade de pessoas que contribuem com a renda mensal', 'required': True}),
            'verificacao_nis' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'NIS', 'required': True}),
            'verificacao_contrato_trabalho' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Contrato de trabalho', 'required': True}),
            'verificacao_ctps' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CTPS', 'required': True}),
            'verificacao_cpf' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CPF', 'required': True}),
            'verificacao_rg' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'RG', 'required': True}),
            'verificacao_endereco' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Endereço', 'required': True}),

            'estado_civil': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Estado civil', 'required': True}),
            'grau_escolaridade': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Grau de escolaridade', 'required': True}),
            'municipio_naturalidade': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Municipio de Naturalidade', 'required': True}),
            'portador_deficiencia': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Portador de deficiência', 'required': True}),
            'raca': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Raça', 'required': True}),
            'tipo_documento_empregador': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Tipo de numeração', 'required': True}),
            'turno_atividade_escolar': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Turno da atividade escolar', 'required': True}),

        }

        fields = (
            'nis_pis',
            'cpf',
            'rg',
            'rg_orgao_exp',
            'rg_uf',
            'nome_completo',
            'nome_mae',
            'nome_pai',
            'dt_nascimento',
            'sexo',
            'titulo_eleitor',
            'ctps',
            'ctps_serie',
            'ctps_uf',
            'cnpj_ultimo_empregador',
            'nome_empresa',
            'funcao',
            'dt_entrada',
            'dt_saida',
            'qtd_filhos_0_m_6_m',
            'qtd_filhos_7_m_3_a',
            'qtd_filhos_4_a_7_a',
            'qtd_filhos_8_a_12_a',
            'qtd_filhos_13_a_17_a',
            'qtd_filhos_18_a_29_a',
            'gestante_familia',
            'alfabetizado',
            'estudando',
            'logradouro',
            'numero',
            'complemento',
            'cep',
            'fone',
            'celular',
            'renda_mensal',
            'qtd_pessoas_casa',
            'qtd_pessoas_contribuem_renda',
            'verificacao_nis',
            'verificacao_contrato_trabalho',
            'verificacao_ctps',
            'verificacao_cpf',
            'verificacao_rg',
            'verificacao_endereco',
            'estado_civil',
            'grau_escolaridade',
            'municipio_naturalidade',
            'portador_deficiencia',
            'raca',
            'tipo_documento_empregador',
            'turno_atividade_escolar',
        )