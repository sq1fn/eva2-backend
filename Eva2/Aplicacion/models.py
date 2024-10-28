from django.db import models

# Create your models here.

class Doctor(models.Model):
    nombre_doctor = models.CharField(max_length=50)
    apellido_doctor = models.CharField(max_length=50)
    rut_doctor = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()
    especialidad = models.CharField(max_length=50)
    correo_doctor = models.EmailField()