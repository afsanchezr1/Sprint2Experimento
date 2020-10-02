from django.db import models
from universidad.models import Universidad

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    id = models.FloatField(null=True, blank=True, default=None)
    universidad = models.OneToOneField(Universidad, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return '{}'.format(self.nombre, self.id, self.universidad.__str__())