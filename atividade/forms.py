# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from atividade.models import Trabalho_campo


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
