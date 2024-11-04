from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro_autor/', views.registrar_autor, name='registro_autor'),
    path('login/', views.login_autor, name='login')
]