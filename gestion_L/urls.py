from django.urls import path
from . import views

urlpatterns = [
    path('Log In/', views.log_in, name="log_in"),
    path('Registro/', views.registro, name="registro"),
    path('Principal/', views.principal, name="principal"),
    path('Lista_Categorias/', views.listar_categorias, name="listar_categorias"),
    path('Lista_Programaciones', views.listar_programaciones, name="listar_programaciones"),
    path('Crear_Programacion', views.crear_programacion, name="crear_programacion"),
    path('agregar_destacado/', views.agregar_destacado, name='agregar_destacado'),
    path('listar_destacados/', views.listar_destacados, name='listar_destacados'),
    path('editar_programacion/<int:pk>/', views.editar_programacion, name='editar_programacion'),
    path('eliminar_programacion/<int:pk>/', views.eliminar_programacion, name='eliminar_programacion'),
]