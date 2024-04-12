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
            'nombre': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),
            'apellido': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),
            'nombre_usuario': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),
            'documento_identidad': forms.NumberInput(attrs={'type':'text',
                                             'class':'form__control'}),
            'edad': forms.NumberInput(attrs={'type':'number',
                                             'class':'form__control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date',
                                                       'class':'form__control'}),

            'rol': forms.Select(attrs={'class':'form__control'}),
            
            'categoria': forms.Select(attrs={'class':'form__control'}),

            'telefono_contacto': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),
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
        