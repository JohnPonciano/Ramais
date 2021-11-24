from django.db import models
from django.utils import timezone
# Create your models here.

# nome: STR * (obrigatório)
# sobrenome: STR (opcional)
# telefone: STR * (obrigatório)
# email: STR (opcional)
# data_criacao: DATETIME (automático)
# descricao: texto
# categoria: CATEGORIA (outro model)

class Categoria(models.Model):
    nome=models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default= timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    photo = models.ImageField(blank=True, upload_to='photos/')
    def __str__(self) :
        return self.nome
