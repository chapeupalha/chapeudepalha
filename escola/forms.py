# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from escola.models import Secretaria, Local, Curso, Turma


class cadastro_local_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_local_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Local

        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o NOME do local', 'required': True, 'style':'z-index:000;'}),
            'endereco': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o ENDEREÇO do local', 'required': True, 'style':'z-index:000;'}),
            'end_numero': forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Numero', 'required': True, 'style':'z-index:000;'}),
            'complemento': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o COMPLEMENTO do endereço', 'style':'z-index:000;'}),
            'cep': forms.TextInput(attrs={'type': 'text', 'class': 'form-control cep_local-js', 'placeholder': 'CEP do local', 'required': True, 'style':'z-index:000;'}),
            'nome_responsavel': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o NOME do responsável', 'required': True, 'style':'z-index:000;'}),
            'tel_responsavel': forms.TextInput(attrs={'type': 'text', 'class': 'form-control mobile-phone-number', 'placeholder': 'TELEFONE do responsável', 'required': True, 'style':'z-index:000;'}),
            'email_responsavel': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'EMAIL do responsável', 'required': True, 'style':'z-index:000;'}),
            'secretaria': forms.CheckboxInput(attrs={'class': 'filled-in chk-col-green', 'id': 'md_checkbox_30', 'style':'z-index:000;'}),
            'municipio_local': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'data-live-search': 'true', 'required': True}),
        }
        fields = (
                'nome',
                'endereco',
                'end_numero',
                'complemento',
                'cep',
                'nome_responsavel',
                'tel_responsavel',
                'email_responsavel',
                'secretaria',
                'municipio_local',
                'status',
                )


class cadastro_secretaria_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_secretaria_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Secretaria

        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o NOME da secretaria', 'required': True}),
            'sigla': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe a SIGLA da secretaria', 'required': True}),
            'nome_responsavel': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o NOME do responsável', 'required': True}),
            'tel_responsavel': forms.TextInput(attrs={'type': 'text', 'class': 'form-control mobile-phone-number', 'placeholder': 'Informe o TELEFONE do responsável', 'required': True}),
            'email_responsavel': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o E-MAIL do responsável', 'required': True}),
        }

        fields = (
                'nome',
                'sigla',
                'nome_responsavel',
                'tel_responsavel',
                'email_responsavel',
                'status',
                )


class cadastro_curso_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_curso_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Curso

        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o NOME do curso', 'required': True, 'style':'z-index:000;'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control no-resize', 'placeholder': ' Descreva o curso', 'required': True}),
            'qtd_horas': forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Informe a quantidade de HORAS', 'required': True, 'style': 'z-index:000;'}),
            'dt_inicio': forms.TextInput(attrs={'type': 'text', 'class': 'form-control datepicker', 'placeholder': 'Informe a DATA DE INÍCIO', 'required': True, 'style': 'z-index:000;'}),
            'dt_final': forms.TextInput(attrs={'type': 'text', 'class': 'form-control datepicker', 'placeholder': 'Informe a DATA DO TÉRMINO', 'required': True, 'style': 'z-index:000;'}),
            'secretaria_curso': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'data-live-search': 'true', 'required': True}),
        }

        fields = (
                'nome',
                'descricao',
                'qtd_horas',
                'dt_inicio',
                'dt_final',
                'secretaria_curso',
                'status',
                )


class cadastro_turma_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(cadastro_turma_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Turma

        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Informe o NOME da turma', 'required': True, 'style':'z-index:000;'}),
            'qtd_aluno_min': forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Qtd. MÍNIMA de alunos', 'required': True, 'style': 'z-index:000;'}),
            'qtd_aluno_max': forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Qtd. MÁXIMA de alunos', 'required': True, 'style': 'z-index:000;'}),
            'turno': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'data-live-search': 'true', 'required': True}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control no-resize', 'placeholder': ' Observações da turma', 'style': 'z-index:000;'}),
            'dia_seg': forms.CheckboxInput(attrs={'class': 'filled-in chk-col-green', 'id': 'md_checkbox_01', 'style': 'z-index:000;'}),
            'dia_ter': forms.CheckboxInput(attrs={'class': 'filled-in chk-col-green', 'id': 'md_checkbox_02', 'style': 'z-index:000;'}),
            'dia_qua': forms.CheckboxInput(attrs={'class': 'filled-in chk-col-green', 'id': 'md_checkbox_03', 'style': 'z-index:000;'}),
            'dia_qui': forms.CheckboxInput(attrs={'class': 'filled-in chk-col-green', 'id': 'md_checkbox_04', 'style': 'z-index:000;'}),
            'dia_sex': forms.CheckboxInput(attrs={'class': 'filled-in chk-col-green', 'id': 'md_checkbox_05', 'style': 'z-index:000;'}),
            'dia_sab': forms.CheckboxInput(attrs={'class': 'filled-in chk-col-red', 'id': 'md_checkbox_06', 'style': 'z-index:000;'}),
            'dia_dom': forms.CheckboxInput(attrs={'class': 'filled-in chk-col-red', 'id': 'md_checkbox_07', 'style': 'z-index:000;'}),
            'curso_turma': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'data-live-search': 'true', 'required': True}),
            'local_turma': forms.Select(attrs={'type': 'select', 'class': 'form-control show-tick', 'data-live-search': 'true', 'required': True}),
        }

        fields = (
                'nome',
                'qtd_aluno_min',
                'qtd_aluno_max',
                'turno',
                'observacoes',
                'dia_seg',
                'dia_ter',
                'dia_qua',
                'dia_qui',
                'dia_sex',
                'dia_sab',
                'dia_dom',
                'curso_turma',
                'local_turma',
                'status',
                )
















