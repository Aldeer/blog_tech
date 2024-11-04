from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, LoginForm


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

def login_autor(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('autores:home')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context=context)