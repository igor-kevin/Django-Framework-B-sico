from django.shortcuts import render


def index(request) -> render:
    context = {
        'curso': 'Programação web com Django Framework',
        'info': 'Mais info para o programa.'
    }
    return render(request, 'index.html', context)


def contato(request) -> render:
    return render(request, 'contato.html')
