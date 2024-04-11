from django import forms
from .models import Jugador, Usuario, Programacion

class DestacadoForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'categoria', 'descripcion', 'foto']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'nombre_usuario', 'documento_identidad', 'edad', 'fecha_nacimiento', 'rol', 'categoria', 'telefono_contacto']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }


class ProgramacionForm(forms.ModelForm):
    class Meta:
        model = Programacion
        fields = ['fecha', 'hora', 'lugar', 'categoria']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'categoria', 'edad', 'documento_identidad']
        