from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

'''
def sobre(request):
    # HTTP Response
    return HttpResponse('<h1>SOBRE - DJANGO</h1>')

def contato(request):
    # HTTP Response
    return HttpResponse('<h1>CONTATO - Django</h1>')
'''
def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Gabriel Rodrigues'})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={})