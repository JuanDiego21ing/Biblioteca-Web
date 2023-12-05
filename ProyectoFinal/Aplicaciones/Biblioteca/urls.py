from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('registrarLibros/', views.registrarLibros),
    path('registrarUsuarios/', views.registrarUsuarios),
    path('registrarAutores/', views.registrarAutores),
    path('registrarEditoriales/', views.registrarEditoriales),
    path('edicionLibro/<id>', views.edicionLibro),
    path('editarLibro/', views.editarLibro),
    path('eliminacionLibro/<id>', views.eliminacionLibro),
    path('gestionUsuarios/', views.gestionUs, name='gestionUs'),
    path('gestionAutores/', views.gestionAu, name='gestionAu'),
    path('gestionEditoriales/', views.gestionEd, name='gestionEd'),
    path('eliminacionUsuario/<str:idUs>/', views.eliminacionUsuario, name='eliminacionUsuario'),
    path('eliminacionAutores/<str:idAu>/', views.eliminacionAutores, name='eliminacionAutores'),
    path('eliminacionEditoriales/<str:idEdi>/', views.eliminacionEditoriales, name='eliminacionEditoriales')
]