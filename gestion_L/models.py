from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='jugadores')
    descripcion = models.TextField()

class Programacion(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, choices=(('sub_baby', 'Sub Baby'), ('sub_8', 'Sub 8'), ('sub_10','Sub 10'), ('sub_11','Sub 11'), ('sub_12','Sub 12'), ('sub_13','Sub 13'), ('sub_14','Sub 14'), ('sub_15','Sub 15'), ('sub_16','Sub 16'), ('ascenso','Ascenso'), ('primera','Primera'), ('femenina','Femenina')))  
    equipo_rival = models.CharField(max_length=100)  # Cambiado a CharField
    resultado_local = models.IntegerField(default=0)
    resultado_visitante = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.lugar}"


class Usuario(models.Model):
    ROLES_CHOICES = (
        ('jugador', 'Jugador'),
        ('profesor', 'Profesor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=150, unique=True)
    nombre = models.CharField(max_length=100)  
    apellido = models.CharField(max_length=100)  
    documento_identidad = models.CharField(max_length=100, unique=True)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=10, choices=ROLES_CHOICES)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.CharField(max_length=100, choices=(('sub_baby', 'Sub Baby'), ('sub_8', 'Sub 8'), ('sub_10','Sub 10'), ('sub_11','Sub 11'), ('sub_12','Sub 12'), ('sub_13','Sub 13'), ('sub_14','Sub 14'), ('sub_15','Sub 15'), ('sub_16','Sub 16'), ('ascenso','Ascenso'), ('primera','Primera'), ('femenina','Femenina')))  # Choices definidos manualmente
    telefono_contacto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def calcular_edad(self):
        today = datetime.now().date()
        birth_date = self.fecha_nacimiento
        age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age_years 
    
    
@receiver(post_delete, sender=Usuario)
def eliminar_usuario_auth_user(sender, instance, **kwargs):
    if hasattr(instance, 'user'):
        instance.user.delete()