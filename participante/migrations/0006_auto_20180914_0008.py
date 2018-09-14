# Generated by Django 2.1.1 on 2018-09-14 03:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0005_auto_20180914_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='alfabetizado',
            field=models.BooleanField(blank=True, null=True, verbose_name='participante é alfabetizado'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='celular',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número de celular do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='cep',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='cep do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='cnpj_ultimo_empregador',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Número do documento do último empregador'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='complemento',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento do endereco do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Número do CPF'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='ctps_uf',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=20, null=True, verbose_name='UF da carteira de trabalho'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='estado_civil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='participante.EstadoCivil', verbose_name='Estado civil do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='estudando',
            field=models.BooleanField(blank=True, null=True, verbose_name='Está estudando'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='fone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número de telefone do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='gestante_familia',
            field=models.BooleanField(blank=True, null=True, verbose_name='Existe gestante na familia'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='grau_escolaridade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='participante.GrauEscolaridade', verbose_name='Grau de escolaridade do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='logradouro',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='municipio_naturalidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Municipio', verbose_name='Naturalidade do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='municipio_participante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='municipio_participante', to='core.Municipio', verbose_name='Municipio do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='nis_pis',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Número do NIS'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='nome_completo',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='nome_mae',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome da Mãe'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='nome_pai',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome do Pai'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='numero',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Número do endereco do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='portador_deficiencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='participante.Deficiencia', verbose_name='Portador de deficiencia'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='qtd_pessoas_casa',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantidade de pessoas que moram na casa'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='qtd_pessoas_contribuem_renda',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantidade de pessoas que contribuem com a renda'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='raca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='participante.Raca', verbose_name='Raça do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='renda_mensal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Renda mensal do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='rg',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Número do RG'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='rg_orgao_exp',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Órgão expedidor do RG'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='rg_uf',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='UF do RG'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('ND', 'Não declarar')], max_length=20, null=True, verbose_name='Sexo do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Status_Geral', verbose_name='Status do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='tipo_documento_empregador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='participante.TipoDocumentoEmpregador', verbose_name='Tipo de documento do empregador'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='titulo_eleitor',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Titulo de eleitor do participante'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='turno_atividade_escolar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='participante.TurnoEscolar', verbose_name='Turno em que esta estudando atualmente'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participante',
            name='usuario_updated',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_update', to=settings.AUTH_USER_MODEL),
        ),
    ]
