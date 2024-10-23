from django.shortcuts import render
from core.models import Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader


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
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context=context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html charset=utf8', status=500)
