from django.urls import path

from . import views

urlpatterns = [
    path('pessoas/', views.index),
    path('cadastros/', views.cadastro),
]