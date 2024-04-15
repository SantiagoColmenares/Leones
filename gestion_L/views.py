from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Programacion, Usuario, User, Jugador
from .forms import DestacadoForm, UsuarioForm, ProgramacionForm, UsuarioEditForm
from datetime import datetime



def principal(request):

    return render(request, 'layouts/principal.html', {})


def log_in(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        documento_identidad = request.POST.get('documento_identidad')

        # Autenticar al usuario utilizando el nombre de usuario y el documento de identidad
        user = authenticate(username=nombre_usuario, password=documento_identidad)

        if user is not None:
            # El usuario fue autenticado con éxito, iniciar sesión
            login(request, user)
            return render(request, 'layouts/principal.html', {})
        else:
            # La autenticación falló, mostrar un mensaje de error o redirigir al formulario de inicio de sesión nuevamente
            return HttpResponse("Inicio de sesión fallido.")
    else:
        # Renderizar el formulario de inicio de sesión
        return render(request, 'login.html')


def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Crear un usuario de Django
            nuevo_usuario = User.objects.create_user(username=form.cleaned_data['nombre_usuario'], password=form.cleaned_data['documento_identidad'])
            if nuevo_usuario:
                # Guardar el formulario asociado al usuario creado
                usuario = form.save(commit=False)
                usuario.user_id = nuevo_usuario.id
                usuario.save()
                return redirect('login')  # Redireccionar a donde quieras después de guardar el formulario
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})

def listar_categorias(request):
    usuarios_baby = Usuario.objects.filter(categoria='Sub Baby')
    usuarios_sub8 = Usuario.objects.filter(categoria='Sub 8')
    usuarios_sub10 = Usuario.objects.filter(categoria='Sub 10')
    usuarios_sub11 = Usuario.objects.filter(categoria='Sub 11')
    usuarios_sub12 = Usuario.objects.filter(categoria='Sub 12')
    usuarios_sub13 = Usuario.objects.filter(categoria='Sub 13')
    usuarios_sub14 = Usuario.objects.filter(categoria='Sub 14')
    usuarios_sub15 = Usuario.objects.filter(categoria='Sub 15')
    usuarios_sub16 = Usuario.objects.filter(categoria='Sub 16')
    usuarios_ascenso = Usuario.objects.filter(categoria='Ascenso')
    usuarios_primera = Usuario.objects.filter(categoria='Primera')
    usuarios_femenina = Usuario.objects.filter(categoria='Femenina')
    es_profesor = False
    if request.user.is_authenticated and hasattr(request.user, 'usuario') and request.user.usuario.rol == 'profesor':
        es_profesor = True
    return render(request, 'list-categorias.html', {'usuarios_primera': usuarios_primera,
                                                    'usuarios_baby':usuarios_baby,
                                                    'usuarios_sub8':usuarios_sub8,
                                                    'usuarios_sub10':usuarios_sub10,
                                                    'usuarios_sub11':usuarios_sub11,
                                                    'usuarios_sub12':usuarios_sub12,
                                                    'usuarios_sub13':usuarios_sub13,
                                                    'usuarios_sub14':usuarios_sub14,
                                                    'usuarios_sub15':usuarios_sub15,
                                                    'usuarios_sub16':usuarios_sub16,
                                                    'usuarios_ascenso':usuarios_ascenso,
                                                    'usuarios_femenina':usuarios_femenina,
                                                    'es_profesor':es_profesor})


def crear_programacion(request):
    profesores = Usuario.objects.filter(rol='Profesor')
    if request.method == 'POST':
        # Si se está enviando el formulario con datos
        form = ProgramacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_programacion')  
    else:
        # Si se está cargando la página por primera vez
        form = ProgramacionForm()
        
    return render(request, 'crear_programacion.html', {'form': form})



@login_required
def listar_programaciones(request):
    programaciones = Programacion.objects.all()
    es_profesor = False  # Por defecto, asumimos que el usuario no es profesor

    # Verificar si el usuario actual tiene el rol de 'profesor'
    if request.user.is_authenticated and hasattr(request.user, 'usuario') and request.user.usuario.rol == 'profesor':
        es_profesor = True

    return render(request, 'list-programaciones.html', {'programaciones': programaciones, 'es_profesor': es_profesor})





def agregar_destacado(request):
    if request.method == 'POST':
        form = DestacadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_destacados')  # Redirige a la página de destacados
    else:
        form = DestacadoForm()
    return render(request, 'destacado.html', {'form': form})


def listar_destacados(request):
    jugadores_destacados = Jugador.objects.all()  # Obtener todos los jugadores destacados
    
    # Verificar si el usuario actual es profesor
    es_profesor = False
    if request.user.is_authenticated and hasattr(request.user, 'usuario') and request.user.usuario.rol == 'profesor':
        es_profesor = True
    
    return render(request, 'listar_destacados.html', {'jugadores_destacados': jugadores_destacados, 'es_profesor': es_profesor})


def editar_programacion(request, pk):
    programacion = get_object_or_404(Programacion, pk=pk)
    
    if request.method == 'POST':
        form = ProgramacionForm(request.POST, instance=programacion)
        if form.is_valid():
            form.save()
            return redirect('listar_programaciones')
    else:
        form = ProgramacionForm(instance=programacion)
        
    return render(request, 'form/editar_programacion.html', {'form': form, 'programacion': programacion})
  # Redirige a la página de listado de programaciones después de editar
    

def eliminar_programacion(request, pk):
    programacion = get_object_or_404(Programacion, pk=pk)
    if request.method == 'POST':
        # Eliminar la programación si se envió una solicitud POST
        programacion.delete()
        return redirect('listar_programaciones')  # Redirige a la página de listado de programaciones después de eliminar
    else:
        # Renderizar la confirmación de eliminación si se accede por GET
        return render(request, 'form/eliminar_programacion.html', {'programacion': programacion})
    

def editar_destacado(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == 'POST':
        # Procesar el formulario de edición si se envió
        form = DestacadoForm(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('listar_destacados')  # Redirige a la página de destacados después de editar
    else:
        # Renderizar el formulario de edición si se accede por GET
        form = DestacadoForm(instance=jugador)
    return render(request, 'form/editar_destacado.html', {'form': form, 'jugador':jugador})

def eliminar_destacado(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == 'POST':
        # Eliminar el jugador si se envió una solicitud POST
        jugador.delete()
        return redirect('listar_destacados')  # Redirige a la página de destacados después de eliminar
    else:
        # Renderizar la confirmación de eliminación si se accede por GET
        return render(request, 'form/eliminar_destacado.html', {'jugador': jugador})
    
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    categorias = ['Primera', 'Femenina', 'Sub Baby', 'Sub 8', 'Sub 10', 'Sub 11','Sub 12','Sub 13','Sub 14','Sub 15','Sub 16', 'Ascenso']   # Obtener todas las categorías
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = UsuarioEditForm(instance=usuario)
        
    return render(request, 'form/editar_usuario.html', {'form': form, 'categorias':categorias, 'usuario':usuario})
    




def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        # Eliminar el usuario si se envió una solicitud POST
        usuario.delete()
        return redirect('listar_categorias')  # Redirige a la lista de usuarios después de eliminar
    else:
        # Renderizar la confirmación de eliminación si se accede por GET
        return render(request, 'form/eliminar_usuario.html', {'usuario': usuario})