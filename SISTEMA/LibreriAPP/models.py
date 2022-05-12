from distutils.command import upload
from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='título')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripcíon', null=True)

    