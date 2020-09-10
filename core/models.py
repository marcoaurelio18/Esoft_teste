from django.db import models
from django.db.models import F


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    idade = models.IntegerField()
    nascimento = models.DateField()
    email = models.EmailField(max_length=256)
    apelido = models.CharField(max_length=128, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)

    @property
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    # Função para retornar o numero do documento no django admin
    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    class Meta:
        ordering = [F('nome').asc(nulls_last=True)]
