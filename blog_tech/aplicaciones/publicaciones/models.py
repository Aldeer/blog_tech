from django.db import models
from ..autores.models import Autor
from ..categorias.models import Categoria



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
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        """
        Metodo que retorna el titulo de la publicacion y a que autor pertenece
        """
        return f'{self.titulo} - '
