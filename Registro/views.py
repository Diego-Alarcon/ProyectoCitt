from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def formulario(request):
    return render(request, 'home/formulario.html')

def reseña(request):
    return render(request, 'home/reseñas.html')

def inicio(request):
    return render(request, 'home/inicio.html')
