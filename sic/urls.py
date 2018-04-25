from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('cadastros/', views.cadastro, name='cadastro_pessoas'),
]