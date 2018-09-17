from django.db import models


class Regiao(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)


class Estado(models.Model):
    codigo_uf = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Municipio(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    uf = models.CharField(max_length=50, blank=True, null=True)
    nome_estado = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        nome_municipio = "[" + str(self.uf) + "] " + str(self.nome)
        return nome_municipio



class Status_Geral(models.Model):
    item = models.CharField(max_length=200, blank=True, null=True)
    chave  = models.CharField(max_length=200, blank=True, null=True)
    texto  = models.CharField(max_length=200, blank=True, null=True)
    next = models.IntegerField(blank=True, null=True)
    ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.texto