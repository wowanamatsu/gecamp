from django.urls import path

from sic.views import paises, pessoas as views

urlpatterns = [
    path('', views.home, name='home'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('cadastros/', views.cadastro, name='cadastro_pessoas'),

    path('paises/', paises.cadastro_pais, name='cadastro_pais'),
]