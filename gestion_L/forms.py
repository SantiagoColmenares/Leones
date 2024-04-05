from django import forms
from .models import Jugador

class DestacadoForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'descripcion', 'foto']
