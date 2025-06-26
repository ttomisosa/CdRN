from django.conf import settings
from django.db import models

class disco(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagen = models.URLField(blank=True, null=True)
    cancion_destacada = models.CharField(max_length=200, blank=True, null=True)
    motivo_destacada = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo