from django.db import models
from fuenteDeDatos.models import FuenteDeDatos

# Create your models here.
class Universidad(models.Model):
    nombre = models.CharField(max_length=50)
    fuenteDeDatos = models.ForeignKey(FuenteDeDatos, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre, self.fuenteDeDatos.__str__())