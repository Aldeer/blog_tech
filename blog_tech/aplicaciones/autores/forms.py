from django import forms
from django.contrib.auth.models import User
from .models import Autor

class UserForm(forms.ModelForm):
    """
    Formulario de registro de usuario comun.
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class AutorForm(forms.ModelForm):
    """
    Clase que genera un formulario para la creacion y validacion de datos
    de autor.
    """

    class Meta:
        model = Autor
        fields = '__all__'