from django.shortcuts import render
from blog.data import response

def blog(request):

    context = {
            'text': 'OLÁ BLOG',
            'posts': response
        }
    
    return render(
        request,
        'blog.html',
        context
    )

def post(request, id):

    context = {
            'text': 'OLÁ BLOG',
            'posts': response
        }
    
    return render(
        request,
        'blog.html',
        context
    )

def exemplo(request):

    context = {
            'text': 'OLÁ EXEMPLO',
            'title': 'Página de Exemplo - '
        }
    
    return render(
        request,
        'exemplo.html',
        context
    )