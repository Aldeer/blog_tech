from django.db import models


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