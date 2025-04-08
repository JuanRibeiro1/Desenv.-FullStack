from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField("Categoria", max_length=200)

    def __str__(self):
        return self.categoria


class Produto(models.Model):
    nomeProduto = models.CharField("Nome do produto", max_length=200)
    valor = models.IntegerField(default=0)
    descricao = models.CharField(max_length=200)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, verbose_name="Categoria"
    )

    def __str__(self):
        return self.nomeProduto