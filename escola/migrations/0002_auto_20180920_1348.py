# Generated by Django 2.1.1 on 2018-09-20 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='dt_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='local',
            name='dt_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='secretaria',
            name='dt_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='turma',
            name='dt_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
