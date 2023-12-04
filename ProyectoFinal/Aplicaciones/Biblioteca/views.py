from django.shortcuts import render, redirect
from . models import libros


# Create your views here.

def home(request):
    librosListas = libros.objects.all()
    return render(request, "gestionLibros.html", {"libros":librosListas})

def registrarLibros(request):
    id=request.POST['txtid']
    titulo=request.POST['txttitulo']
    autor=request.POST['txtautor']
    editorial=request.POST['txtedito']
    fecha=request.POST['datefecha']
    genero=request.POST['txtgen']

    Libros = libros.objects.create(id=id,titulo=titulo,autor=autor,editorial=editorial,fecha=fecha,genero=genero)
    return redirect('/')

def edicionLibro(request, id):
    Libros = libros.objects.get(id=id)
    return render(request, "edicionLibro.html", {"Libro": Libros})

def editarLibro(request):
    id=request.POST['txtid']
    titulo=request.POST['txttitulo']
    autor=request.POST['txtautor']
    editorial=request.POST['txtedito']
    fecha=request.POST['datefecha']
    genero=request.POST['txtgen']

    Libros = libros.objects.get(id=id)
    Libros.id = id
    Libros.titulo = titulo
    Libros.autor = autor
    Libros.editorial = editorial
    Libros.fecha = fecha
    Libros.genero = genero
    Libros.save()

    return redirect('/')

def eliminacionLibro(request, id):
    Libros = libros.objects.get(id=id)
    Libros.delete()
    return redirect('/')
