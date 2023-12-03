from django.shortcuts import render
from . models import libros

# Create your views here.

def home(request):
    librosListas = libros.objects.all()
    return render(request, "gestionLibros.html", {"libros":librosListas})
