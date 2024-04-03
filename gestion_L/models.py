from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)



class Programacion(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=100)
    profesor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Usuario(models.Model):
    ROLES_CHOICES = (
        ('jugador', 'Jugador'),
        ('profesor', 'Profesor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    documento = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=10, choices=ROLES_CHOICES)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.CharField(max_length=100, choices=(('sub_baby', 'Sub Baby'), ('sub_8', 'Sub 8'), ('sub_10','Sub 10'), ('sub_11','Sub 11'), ('sub_12','Sub 12'), ('sub_13','Sub 13'), ('sub_14','Sub 14'), ('sub_15','Sub 15'), ('sub_16','Sub 16'), ('ascenso','Ascenso'), ('primera','Primera'), ('femenina','Femenina')))  # Choices definidos manualmente
    telefono_contacto = models.CharField(max_length=100)

