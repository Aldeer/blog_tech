from django.db import models


class Publicacion(models.Model):
    """
    Class modelo de Publicacion
    campos:
        - id_publicacion:
        - titulo:
        - descripcion:
        - contenido:
        - portada:
        - creado:
        - actualizado:
        - estado:
        - id_autor:
    """

    id_publicacion = models.AutoField(primary_key=True, verbose_name='ID Publicacion')
    titulo = models.CharField(verbose_name='Titulo', max_length=255, blank=False, null=False)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=255, blank=False, null=False)
    contenido = models.TextField(verbose_name='Contenido', blank=False, null=False)
    portada = models.URLField(verbose_name='Portada', max_length=255, blank=False, null=False)
    creado = models.DateTimeField(verbose_name='Fecha Publicacion', auto_now=False, auto_now_add=True)
    actualizado = models.DateTimeField(verbose_name='Ultima actualizacion', auto_now=True, auto_now_add=False)
    estado = models.BooleanField(verbose_name='Publicacion activa', default=True)


    def __str__(self):
        """
        Metodo que retorna el titulo de la publicacion y a que autor pertenece
        """
        return f'{self.titulo} - '
