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
