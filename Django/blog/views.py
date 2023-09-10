from django.shortcuts import render
from blog.data import response
from typing import Any
from django.http import HttpRequest, Http404

def blog(request):

    context = {
            'text': 'OLÁ BLOG',
            'posts': response,
        }
    
    return render(
        request,
        'blog.html',
        context
    )

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in response:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não encontrado!')

    context = {
            # 'text': '',
            'post': found_post,
            'title': found_post['title'] + ' - ',
        }
    
    return render(
        request,
        'post.html',
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