from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import Autor

class UserForm(forms.ModelForm):
    """
    Formulario de registro de usuario comun.
    """

    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    confirm_pass = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')

    class Meta:
        model = User
        fields = ('username', 'email')

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_pass = cleaned_data.get('confirm_pass')

        if password != confirm_pass:
            raise forms.ValidationError('Las contraseñas no coinciden')
        
    def save(self):
        usuario = super().save()
        usuario.set_password(self.cleaned_data.get('password'))
        usuario.is_staff = False
        usuario.is_superuser = False
        usuario.save()

        autor = Autor.objects.create(usuario=usuario)
        return usuario