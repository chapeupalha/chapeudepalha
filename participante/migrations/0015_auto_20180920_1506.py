# Generated by Django 2.1.1 on 2018-09-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0014_documentosparticipante_tipo_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='dt_cadastro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
