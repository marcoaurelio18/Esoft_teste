from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    idade = models.IntegerField()
    nascimento = models.DateField()
    email = models.EmailField(max_length=256)
    apelido = models.CharField(max_length=128, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)