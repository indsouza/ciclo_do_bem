# gerenciador/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def saiba_mais(request):
    return render(request, 'saiba_mais.html')

