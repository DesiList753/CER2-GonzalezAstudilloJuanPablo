from django.db import models
from django.contrib.auth.models import User
# Create your models here.


TIPO_CHOICES = [("S", "SUSPENSION_ACTIVIDADES"),("C", "SUSPENSION_CLASE INFORMACION"),("T","Informacion")]

class Entidad(models.Model):
    id_entidad = models.BigAutoField(primary_key=True)
    nombre_entidad = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='USM_WEB/img/logo_entidad/', blank=True, null=True)

    def __str__(self):
        return self.nombre_entidad

class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=500)
    detalle_corto = models.CharField(max_length=100)
    tipo = models.CharField(max_length = 1,choices = TIPO_CHOICES, default="S")
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    publicacion_por = User
    modificado_por = User
    
    def __str__(self):
        return self.titulo
