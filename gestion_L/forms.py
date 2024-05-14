from django import forms
from datetime import datetime, date
from .models import Jugador, Usuario, Programacion

class DestacadoForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'categoria', 'descripcion', 'foto']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'nombre_usuario', 'documento_identidad', 'fecha_nacimiento', 'edad', 'rol', 'categoria', 'telefono_contacto']
        widgets = {
            'nombre': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),
            'apellido': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),
            'nombre_usuario': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control',
                                             'data-error-target': '#username-error'}),
            'documento_identidad': forms.NumberInput(attrs={'type':'text',
                                             'class':'form__control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date',
                                                       'class':'form__control',
                                                       }),

            'edad': forms.NumberInput(attrs={'type':'number',
                                             'class':'form__control',
                                             'readonly':'readonly'
                                            }),
            

            'rol': forms.Select(attrs={'class':'form__control'}),
            
            'categoria': forms.Select(attrs={'class':'form__control'}),

            'telefono_contacto': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),
        }

    def clean(self):
    # Obtener los valores limpios de los campos
        cleaned_data = super().clean()
        edad = cleaned_data.get('edad')
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')
    # Validar que la edad coincida con la fecha de nacimiento
        if edad is not None and fecha_nacimiento is not None:
        # Convertir la fecha de nacimiento a una fecha de tipo date
            fecha_nacimiento_date = fecha_nacimiento
        # Calcular la edad real en base a la fecha de nacimiento
            today = date.today()
            edad_real = today.year - fecha_nacimiento_date.year
        # Ajustar la edad si el cumpleaños no ha ocurrido este año
            if (today.month, today.day) < (fecha_nacimiento_date.month, fecha_nacimiento_date.day):
                edad_real -= 1
        # Verificar si la edad ingresada coincide con la edad calculada
            if edad != edad_real:
                self.add_error('edad', 'La edad no coincide con la fecha de nacimiento')
                self.add_error('fecha_nacimiento', 'La edad no coincide con la fecha de nacimiento')
        return cleaned_data
        
    def clean_documento_identidad(self):
        documento_identidad = self.cleaned_data['documento_identidad']
        if Usuario.objects.filter(documento_identidad=documento_identidad).exists():
            self.add_error('documento_identidad', 'El documento de identidad ya existe en la base de datos')
        return documento_identidad

    def calcular_edad(self):
        today = datetime.now().date()
        birth_date = self.fecha_nacimiento
        age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age_years


class ProgramacionForm(forms.ModelForm):
    class Meta:
        model = Programacion
        fields = ['fecha', 'hora', 'lugar', 'categoria', 'equipo_rival', 'resultado_local', 'resultado_visitante']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'equipo_rival':forms.TextInput(attrs={'type':'text'})
        }

class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'categoria', 'edad', 'documento_identidad']
        widgets = {
            'edad': forms.NumberInput(attrs={'type': 'number',
                                           'readonly':'readonly'})
        }
        

        