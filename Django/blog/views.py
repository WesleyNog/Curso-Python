from django.shortcuts import render
# from django.http import HttpResponse


def blog(request):
    return render(
        request,
        'blog.html'
    )

def exemplo(request):
    return render(
        request,
        'exemplo.html'
    )