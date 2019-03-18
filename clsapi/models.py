from django.db import models



class Estabelecimento(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

class Unidade(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

class Filtro(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

