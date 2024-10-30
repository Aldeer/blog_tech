from django.db import models


class Categoria(models.Model):
    """
    Clase model de Categoria
    Campos:
        - id_categoria:
        - nombre:
        - id_publicacion:
    """

    id_categoria = models.AutoField(primary_key=True, verbose_name='ID Categoria')
    nombre = models.CharField(verbose_name='Nombre Categoria', max_length=255, blank=False, null=False)
    


