from django.urls import path

from .views import *

urlpatterns = [
    path('veterinaria', VeterinariaController.as_view()),
    path('veterinaria/<int:id>', ActualizarVeterinariaController.as_view()),
    path('veterinario', VeterinariosController.as_view())
]