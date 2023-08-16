from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def code(request):
    return HttpResponse('<h1>Greatest apologies, Stevens is currently indisposed.</h1>')
