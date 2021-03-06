# Generated by Django 2.1.1 on 2018-09-13 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deficiencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=500, verbose_name='Nome da Deficiência')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=500, verbose_name='Nome do estado civil')),
            ],
        ),
        migrations.CreateModel(
            name='GrauEscolaridade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=500, verbose_name='Nome do grau da escolaridade')),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=500, verbose_name='Nome da raça do participante')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumentoEmpregador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=500, verbose_name='Nome do tipo de documento do empregador')),
            ],
        ),
        migrations.CreateModel(
            name='TurnoEscolar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=500, verbose_name='Nome do Turno')),
            ],
        ),
    ]
