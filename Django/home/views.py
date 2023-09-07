from django.shortcuts import render
# from django.http import HttpResponse

def home(request):

    context = {
            'text': 'OLÁ HOME'
        }
    
    return render(
        request,
        'index.html',
        context
    )