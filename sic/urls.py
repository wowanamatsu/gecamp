from django.urls import path

from . import views

urlpatterns = [
    path('pessoas/', views.index, name='pessoas'),
    path('cadastros/', views.cadastro, name='cadastro_pessoas'),
]