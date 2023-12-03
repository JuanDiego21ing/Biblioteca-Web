from django.db import models

# Create your models here.

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

