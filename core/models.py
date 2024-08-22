from django.db import models


class Produto(models.Model):
    nome: str = models.CharField('Nome', max_length=100)
    preco: float = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque: int = models.IntegerField('Quantidade em Estoque')


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
