from django.contrib import admin
from .models import libros
from .models import Usuarios
from .models import Autores

# Register your models here.

admin.site.register(libros)
admin.site.register(Usuarios)
admin.site.register(Autores)
