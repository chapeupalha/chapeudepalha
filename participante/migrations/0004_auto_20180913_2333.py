# Generated by Django 2.1.1 on 2018-09-14 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0003_participante_nome_completo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, verbose_name='Número do CPF'),
        ),
    ]