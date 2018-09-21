# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from participante.models import Participante, DocumentosParticipante
from core.choices import CHOICES_SEXO, CHOICES_UF


class cadastro_participante(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_participante, self).__init__(*args, **kwargs)

    class Meta:
        model = Participante

        widgets = {
            'nome_completo' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o nome completo do beneficiário', 'required': True}),
            'cpf' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control cpf_input', 'placeholder': 'Informe o CPF do beneficiário', 'required': True}),
        }

        fields = ('cpf', 'nome_completo', 'status', 'usuario',)


class cadastro_dados_participante(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_dados_participante, self).__init__(*args, **kwargs)

    class Meta:
        model = Participante

        widgets = {
            'nis_pis' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o NIS/PIS', 'required': True}),
            'cpf': forms.TextInput(attrs={'type': 'text', 'class': 'form-control cpf_input', 'placeholder': 'Informe o CPF', 'required': True}),
            'rg' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o RG', 'required': True}),
            'rg_orgao_exp' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o Órgão expedidor', 'required': True}),
            'rg_uf' : forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'Informe o UF do órgão expedidor', 'required': True}),
            'nome_completo': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o Nome completo', 'required': True}),
            'nome_mae' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o Nome da Mãe', 'required': True}),
            'nome_pai': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o Nome de Pai'}),
            'dt_nascimento' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control date_input', 'placeholder': 'Informe a Data de nascimento', 'required': True}),
            'sexo' : forms.Select(attrs={'type': 'select', 'required': True, 'class': 'form-control'}, choices=CHOICES_SEXO),
            'titulo_eleitor' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o Título de eleitor', 'required': True}),
            'ctps' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o Nº da CTPS'}),
            'ctps_serie' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe a Série da CTPS'}),
            'ctps_uf' : forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'UF da ctps'}),
            'cnpj_ultimo_empregador' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o CNPJ/CEI/CPF do último empregador'}),
            'nome_empresa' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o Nome da empresa (Razão social)'}),
            'funcao' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe a Função'}),
            'dt_entrada' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control date_input', 'placeholder': 'Informe a data de entrada'}),
            'dt_saida' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control date_input', 'placeholder': 'Informe a data de saída'}),
            'qtd_filhos_0_m_6_m' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 0 a 6 meses' }),
            'qtd_filhos_7_m_3_a' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 7 meses a 3 anos'}),
            'qtd_filhos_4_a_7_a' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 4 a 7 anos'}),
            'qtd_filhos_8_a_12_a' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 8 a 12 anos'}),
            'qtd_filhos_13_a_17_a' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 13 a 17 anos'}),
            'qtd_filhos_18_a_29_a' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'De 18 a 29 anos'}),
            'gestante_familia' : forms.Select(attrs={'type': 'select', 'class': 'form-control' }),
            'alfabetizado' : forms.Select(attrs={'type': 'select', 'class': 'form-control' }),
            'estudando' : forms.Select(attrs={'type': 'select', 'class': 'form-control' }),
            'logradouro' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o Logradouro', 'required': True}),
            'numero' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nº'}),
            'complemento' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o Complemento'}),
            'cep' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control cep_input', 'placeholder': 'Informe o CEP', 'required': True}),
            'fone' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control fone_input', 'placeholder': 'Informe o Telefone'}),
            'celular' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control fone_input', 'placeholder': 'Informe o Celular'}),
            'renda_mensal' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe a Renda Mensal', 'required': True}),
            'qtd_pessoas_casa' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Quantas pessoas que moram na casa', 'required': True}),
            'qtd_pessoas_contribuem_renda' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Quantas pessoas que contribuem com a renda mensal', 'required': True}),
            # 'verificacao_nis' : forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'NIS'}),
            # 'verificacao_contrato_trabalho' : forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Contrato de trabalho'}),
            # 'verificacao_ctps' : forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'CTPS'}),
            # 'verificacao_cpf' : forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            # 'verificacao_rg' : forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'RG'}),
            # 'verificacao_endereco' : forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),

            'estado_civil': forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'Estado civil', 'required': True}),
            'grau_escolaridade': forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'Grau de escolaridade', 'required': True}),
            'municipio_naturalidade': forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'Municipio de Naturalidade', 'required': True}),
            'municipio_participante': forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'Municipio do Participante', 'required': True}),
            'portador_deficiencia': forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'Portador de deficiência'}),
            'raca': forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'Raça'}),
            'tipo_documento_empregador': forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'Tipo de numeração'}),
            'turno_atividade_escolar': forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'Turno da atividade escolar', 'required': True}),

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
            'municipio_participante',
            'portador_deficiencia',
            'raca',
            'tipo_documento_empregador',
            'turno_atividade_escolar',
        )


class cadastro_dados_representante_legal(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_dados_representante_legal, self).__init__(*args, **kwargs)

    class Meta:
        model = Participante

        widgets = {
            'representante_legal_nis_pis' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'NIS/PIS do representante legal', 'required': True}),
            'representante_legal_cpf': forms.TextInput(attrs={'type': 'text', 'class': 'form-control cpf_input', 'placeholder': 'CPF do representante legal', 'required': True}),
            'representante_legal_nome': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome completo do representante legal', 'required': True}),
            'representante_legal_dt_nascimento' : forms.TextInput(attrs={'type': 'text', 'class': 'form-control date_input', 'placeholder': 'Data de nascimento', 'required': True}),

        }

        fields = (
            'representante_legal_nis_pis',
            'representante_legal_cpf',
            'representante_legal_nome',
            'representante_legal_dt_nascimento',
        )


class cadastro_copia_documentos(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_copia_documentos, self).__init__(*args, **kwargs)

    class Meta:
        model = DocumentosParticipante

        widgets = {
            'tipo_documento' : forms.Select(attrs={'type': 'select', 'class': 'form-control', 'placeholder': 'Tipo de Documento', 'required': True}),
            'documento': forms.FileInput(attrs={'required': True}),

        }

        fields = (
            'tipo_documento',
            'documento',
        )