# from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    return HttpResponse('Blog do app 1')

def exemplo(request):
    return HttpResponse('exemplo do app 1')