from django.db import models

# Create your models here.

# gestion Libros

class libros(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editorial = models.CharField(max_length=200)
    fecha = models.DateField(max_length=200)
    genero = models.CharField(max_length=200)

    def __str__(self):
        texto = "{0} ({1}) ({2}) ({3}) ({4}) ({5})"
        return texto.format(self.id,self.titulo,self.autor,self.editorial,self.fecha,self.genero)
    
# gestion Usuarios

class Usuarios(models.Model):
    idUs = models.CharField(primary_key=True, max_length=6)
    nomUsu = models.CharField(max_length=200)
    apellUsu = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)

# gestion Autores

class Autores(models.Model):
    idAu = models.CharField(primary_key=True, max_length=6)
    nomAu = models.CharField(max_length=200)
    apellAu = models.CharField(max_length=200)
    
    


