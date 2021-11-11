from django.shortcuts import render


def index(request): #Requisitando a página ao Django.
    return render(request, 'index.html')

def livro(request):
    return render(request, 'livro.html')
