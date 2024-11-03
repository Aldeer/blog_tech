from django.shortcuts import render, redirect
from .forms import UserForm


def home(request):
    return render(request, 'index.html')

def registrar_autor(request):
    
    if request.method == 'POST':
        registro_form = UserForm(request.POST)
        if registro_form.is_valid():
            registro_form.save()
            return redirect('autores:home')
    else:
        registro_form = UserForm()
    
    context = {'registro_form': registro_form}
    return render(request, 'registro_autor.html', context)