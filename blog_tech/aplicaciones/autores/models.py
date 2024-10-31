from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    """
    Clase modelo de autores
    """

    id_autor = models.AutoField(primary_key=True, verbose_name='ID Autor')
    usuario = models.OneToOneField(User, verbose_name='Usuario', on_delete=models.CASCADE)


    def __str__(self):
        """
        Retorna el nobmre de usuario del autor
        """
        return f'{self.usuario.username}'