from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('registrarLibros/', views.registrarLibros),
    path('edicionLibro/<id>', views.edicionLibro),
    path('editarLibro/', views.editarLibro),
    path('eliminacionLibro/<id>', views.eliminacionLibro)

]