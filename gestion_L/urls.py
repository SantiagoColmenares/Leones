from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('Registro/', views.registro, name="registro"),
    path('Principal/', views.principal, name="principal"),
    path('Lista_Categorias/', views.listar_categorias, name="listar_categorias"),
    path('Lista_Programaciones', views.listar_programaciones, name="listar_programaciones"),
    path('Crear_Programacion', views.crear_programacion, name="crear_programacion"),
    path('agregar_destacado/', views.agregar_destacado, name='agregar_destacado'),
    path('listar_destacados/', views.listar_destacados, name='listar_destacados'),
    path('editar_programacion/<int:pk>/', views.editar_programacion, name='editar_programacion'),
    path('eliminar_programacion/<int:pk>/', views.eliminar_programacion, name='eliminar_programacion'),
    path('editar_destacado/<int:pk>/', views.editar_destacado, name='editar_destacado'),
    path('eliminar_destacado/<int:pk>/', views.eliminar_destacado, name='eliminar_destacado'),
    path('editar_usuario/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
]