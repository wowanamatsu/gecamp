from django.urls import path

from sic.views import paises, pessoas as views

urlpatterns = [
    path('', views.home, name='home'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('pessoa/nova/', views.cadastro, name='cadastro_pessoas'),

    path('paises/', paises.index, name='paises'),
    path('pais/novo/', paises.cadastro, name='cadastro_pais'),
]