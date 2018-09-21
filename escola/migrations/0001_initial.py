# Generated by Django 2.1.1 on 2018-09-19 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_status_geral'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=500, verbose_name='Nome do curso')),
                ('descricao', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Descrição do curso')),
                ('qtd_horas', models.IntegerField(blank=True, null=True, verbose_name='Quantidade de horas')),
                ('dt_inicio', models.DateTimeField(blank=True, null=True, verbose_name='Data de inicio')),
                ('dt_final', models.DateTimeField(blank=True, null=True, verbose_name='Data Final')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=500, verbose_name='Nome do local')),
                ('endereco', models.CharField(blank=True, max_length=500, verbose_name='Logradouro')),
                ('end_numero', models.IntegerField(blank=True, null=True, verbose_name='Numero')),
                ('complemento', models.CharField(blank=True, max_length=500, verbose_name='Complemento')),
                ('cep', models.CharField(blank=True, max_length=500, verbose_name='CEP')),
                ('nome_responsavel', models.CharField(blank=True, max_length=500, verbose_name='Nome do responsável')),
                ('tel_responsavel', models.CharField(blank=True, max_length=500, verbose_name='Tel do responsável')),
                ('email_responsavel', models.CharField(blank=True, max_length=500, verbose_name='E-mail do responsável')),
                ('secretaria', models.BooleanField(default=False, verbose_name='Local disponibilizado para secretaria')),
                ('municipio_local', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Municipio', verbose_name='Municipio')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Status_Geral')),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=500, verbose_name='Nome da secretaria')),
                ('sigla', models.CharField(blank=True, max_length=20, verbose_name='Sigla da secretaria')),
                ('nome_responsavel', models.CharField(blank=True, max_length=500, verbose_name='Nome do responsável')),
                ('tel_responsavel', models.CharField(blank=True, max_length=500, verbose_name='Tel do responsável')),
                ('email_responsavel', models.CharField(blank=True, max_length=500, verbose_name='E-mail do responsável')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Status_Geral')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=500, verbose_name='Nome da turma')),
                ('qtd_aluno_min', models.IntegerField(blank=True, null=True, verbose_name='Quantidade maxima de alunos')),
                ('qtd_aluno_max', models.IntegerField(blank=True, null=True, verbose_name='Quantidade minima de alunos')),
                ('turno', models.CharField(blank=True, choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno')], default='Matutino', max_length=20, null=True, verbose_name='Turno escolar')),
                ('observacoes', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Observações')),
                ('dia_seg', models.BooleanField(default=False, verbose_name='Segunda-Feira')),
                ('dia_ter', models.BooleanField(default=False, verbose_name='Terça-Feira')),
                ('dia_qua', models.BooleanField(default=False, verbose_name='Quarta-Feira')),
                ('dia_qui', models.BooleanField(default=False, verbose_name='Quinta-Feira')),
                ('dia_sex', models.BooleanField(default=False, verbose_name='Sexta-Feira')),
                ('dia_sab', models.BooleanField(default=False, verbose_name='Sábado')),
                ('dia_dom', models.BooleanField(default=False, verbose_name='Domingo')),
                ('curso_turma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escola.Curso')),
                ('local_turma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escola.Local')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Status_Geral')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='secretaria_curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escola.Secretaria'),
        ),
        migrations.AddField(
            model_name='curso',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Status_Geral'),
        ),
    ]
