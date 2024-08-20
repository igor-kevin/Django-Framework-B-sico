from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contato(request) -> render:
    return render(request, 'contato.html')
