from django.shortcuts import render
from core.models import Produto


def index(request) -> render:
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação web com Django Framework',
        'info': 'Mais info para o programa.',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request) -> render:
    return render(request, 'contato.html')


def produto(request, pk) -> render:
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context=context)
