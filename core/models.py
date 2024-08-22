from django.db import models


class Produto(models.Model):
    nome: str = models.CharField('Nome', max_length=100)
    preco: float = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque: int = models.IntegerField('Quantidade em Estoque')
