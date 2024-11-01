from django.shortcuts import render
from .forms import AutorForm, UserForm


def home(request):
    return render(request, 'index.html')

def registrar_autor(request):
    
    if request.method == 'POST':
        pass
    autor_form = AutorForm()
    user_form = UserForm()
    context = {'autor_form': autor_form, 'user_form': user_form}
    return render(request, 'registro_autor.html', context)