from django.urls import path

from .views import *

urlpatterns = [
    path('veterinaria', VeterinariaController.as_view()),
    path('veterinaria/<int:id>', ActualizarVeterinariaController.as_view()),
    path('veterinario', VeterinariosController.as_view()),
    path('veterinario/<int:id>', veterinarioController.as_view()),
    path('servicio', serviciosController.as_view()),
    path('registro', RegistroUsuariosController.as_view())
]