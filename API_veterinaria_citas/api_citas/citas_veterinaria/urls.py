from django.urls import path

from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('veterinaria', VeterinariaController.as_view()),
    path('veterinaria/<int:id>', ActualizarVeterinariaController.as_view()),
    path('veterinario', VeterinariosController.as_view()),
    path('veterinario/<int:id>', veterinarioController.as_view()),
    path('servicio', serviciosController.as_view()),
    path('servicio/<int:id>', ServicioController.as_view()),
    path('registro', RegistroUsuariosController.as_view()),
    path('login_custom', CustomPayloadController.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path("mascota", MascotasController.as_view()),
    path("mascota/<int:id>", MascotaController.as_view()),
    path("traerMascotadelUsuario/<int:id>", MascotaDelUsuarioPorId.as_view()),
    path("citas", CitasController.as_view()),
    path("citass", TraerCitasDeUsuarioController.as_view())
]