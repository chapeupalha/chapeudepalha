#_x -- coding: utf8 --
# vim: set fileencoding=utf8 :
from django.db import models


def generate_name_file():

    return 'teste'


class Documento(models.Model):
    foto_perfil = models.FileField(max_length=1000, upload_to='teste', null=True, blank=True,
                                   default="usuario/perfil_default.png", verbose_name=u"BUSCAR ARQUIVO NO COMPUTADOR")
