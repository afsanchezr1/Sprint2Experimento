from django.db import models

# Create your models here.

class Estadisticas(models.Model):
    vistas = models.FloatField(null=True, blank=True, default=None)
    tiempoPromedioVista = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '%s %s' % (self.vistas, self.tiempoPromedioVista)