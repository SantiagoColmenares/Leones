# Generated by Django 5.0.3 on 2024-04-03 16:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('entrenador', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('lugar', models.CharField(max_length=100)),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=150, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('documento_identidad', models.CharField(max_length=100, unique=True)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('rol', models.CharField(choices=[('jugador', 'Jugador'), ('profesor', 'Profesor')], max_length=10)),
                ('categoria', models.CharField(choices=[('sub_baby', 'Sub Baby'), ('sub_8', 'Sub 8'), ('sub_10', 'Sub 10'), ('sub_11', 'Sub 11'), ('sub_12', 'Sub 12'), ('sub_13', 'Sub 13'), ('sub_14', 'Sub 14'), ('sub_15', 'Sub 15'), ('sub_16', 'Sub 16'), ('ascenso', 'Ascenso'), ('primera', 'Primera'), ('femenina', 'Femenina')], max_length=100)),
                ('telefono_contacto', models.CharField(max_length=100)),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_L.equipo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
