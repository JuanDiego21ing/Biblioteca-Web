from django.shortcuts import render, redirect
from . models import libros
from . models import Usuarios
from . models import Autores


# Create your views here.

#-------- vistas de Libros-----------------------------------------------------------
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

# -------- vistas de Usuarios-----------------------------------------------------------
def gestionUs(request):
    UsuariosListas = Usuarios.objects.all()
    return render(request, 'gestionUsuarios.html', {"Usuarios":UsuariosListas})

def registrarUsuarios(request):
    idUs=request.POST['txtidU']
    nomUsu=request.POST['txtNomUsu']
    apellUsu=request.POST['txtapeUsu']
    correo=request.POST['txtemailUsu']

    usuarios = Usuarios.objects.create(idUs=idUs,nomUsu=nomUsu,apellUsu=apellUsu,correo=correo)
    return redirect('/gestionUsuarios/')

# -------- vistas de Autores-----------------------------------------------------------
def gestionAu(request):
    AutoresListas = Autores.objects.all()
    return render(request, 'gestionAutores.html', {"Autores":AutoresListas})

def registrarAutores(request):
    idAu=request.POST['txtidA']
    nomAu=request.POST['txtNomAut']
    apellAu=request.POST['txtapeAut']
    
    usuarios = Autores.objects.create(idAu=idAu,nomAu=nomAu,apellAu=apellAu)
    return redirect('/gestionAutores/')


# -------- vistas de Editoriales-----------------------------------------------------------
def gestionEd(request):
    return render(request, 'gestionEditoriales.html')