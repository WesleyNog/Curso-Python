from django.shortcuts import render
# from django.http import HttpResponse


def blog(request):

    context = {
            'text': 'OLÁ BLOG'
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