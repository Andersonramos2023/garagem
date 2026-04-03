from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, blank=True, null=True)
    categoria = models.CharField(max_length=80, blank=True, null=True)

def __str__(self):
    marca_up = (self.marca or "").upper()
    nome_up = self.nome.upper()
    return f"{self.id} - {nome_up} {marca_up}"