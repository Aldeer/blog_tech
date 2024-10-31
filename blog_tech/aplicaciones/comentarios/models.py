from django.db import models
from ..autores.models import Autor
from ..publicaciones.models import Publicacion


class Comentario(models.Model):
    """
    Clase modelo de Comentario
    Campos:
        - id_comentario:
        - comentario:
        - id_publicacion:
        - id_autor:
    """

    comentario = models.TextField(verbose_name='Comentario')
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


    def __str__(self):
        """
        Retorna el nombre del autor y el titulo de la publicacion a la
        que pertenece el comentario.
        """
        return f'{self.id_autor.usuario.username} - {self.id_publicacion.titulo}'