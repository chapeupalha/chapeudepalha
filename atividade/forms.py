# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from atividade.models import Trabalho_campo, Ocorrencia, Tarefa_correncia


class cadastro_atividade_trabalho(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_atividade_trabalho, self).__init__(*args, **kwargs)

    class Meta:
        model = Trabalho_campo

        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome da Atividade de Trabalho', 'required': True}),
            'descricao': forms.Textarea(attrs={'type': 'text', 'class': 'form-control no-resize', 'required': True}),
            'at_equipe_trabalho': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'required': True}),
            'at_unidade_gestora': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'required': True}),
            'at_tipo_atividade': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'required': True}),
            'at_municipio': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'required': True}),
        }

        fields = (
                'nome',
                'descricao',
                'at_equipe_trabalho',
                'at_unidade_gestora',
                'at_tipo_atividade',
                'user_created',
                'at_municipio',
                'at_status',
                )


class cadastro_ocorrencia_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_ocorrencia_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Ocorrencia

        widgets = {
            'nome_solicitante': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o nome do solicitante', 'required': True}),
            'tel_solicitante': forms.TextInput(attrs={'type': 'text', 'class': 'form-control mobile-phone-number', 'placeholder': 'Informe o telefone no solicitante', 'required': True}),
            'email_solicitante': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o e-mail do solicitante', 'required': True}),
            'questionamento': forms.Textarea(attrs={'class': 'form-control no-resize', 'placeholder': 'Digite aqui a descrição da ocorrência', 'required': True}),
            'equipe_responsavel': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'data-live-search': 'true', 'required': True}),
            'beneficiario_participante': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'data-live-search': 'true', 'required': True}),
            'municipio': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'data-live-search': 'true', 'required': True}),
        }

        fields = (
                'num_protocolo',
                'dt_solicitacao',
                'nome_solicitante',
                'tel_solicitante',
                'email_solicitante',
                'beneficiario_participante',
                'questionamento',
                'user_atendente',
                'equipe_responsavel',
                'status',
                'municipio',
                )


class cadastro_solucao_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_solucao_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Tarefa_correncia

        widgets = {
            'titulo': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o titulo da solução', 'required': True}),
            'solucao': forms.Textarea(
                attrs={'class': 'form-control no-resize', 'placeholder': 'Digite aqui como ocorreu a solução', 'required': True}),
            'equipe_responsavel_solucao': forms.Select(
                attrs={'class': 'form-control show-tick', 'data-live-search': 'true', 'required': True}),
            'dt_solucao': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control date_solucao', 'placeholder': 'Ex: 30/07/2018', 'required': True}),
        }

        fields = (
                'ocorrencia',
                'titulo',
                'solucao',
                'dt_solucao',
                'equipe_responsavel_solucao',
                )
