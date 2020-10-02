from django.db import models
from estadisticas.models import Estadisticas
# Create your models here.

class FuenteDeDatos(models.Model):
    nombre = models.CharField(max_length=50)
    estadisticas = models.OneToOneField(Estadisticas, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return '{}'.format(self.nombre, self.estadisticas.__str__())
