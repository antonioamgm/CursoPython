from django.db import models
from django.utils import timezone
# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.CharField(max_length=2000)
    fecha = models.DateTimeField('Fecha de publicación')

    def __str__(self):
        return self.titulo
    def publicada_hoy(self):
        return self.fecha.date() == timezone.now().date()

    publicada_hoy.boolean = True
    publicada_hoy.descripcion_corta = '¿Introducida hoy?'

class Comentario(models.Model):
    entrada = models.ForeignKey(Entrada)
    contenidocomentario = models.CharField(max_length=2000)