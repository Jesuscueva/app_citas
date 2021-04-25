"""api_citas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.permissions import AllowAny

documentation_view = get_schema_view(
    info = openapi.Info(
        title="Citas Veterinaria",
        default_version="1.0",
        description="Veterinaria API",
        contact= openapi.Contact(
            email="jcueva12380@gmail.com", name="Jesus Cueva"
        ),
    ),
    public=True,
    permission_classes=[AllowAny, ]
)

urlpatterns = [
    path("api/docs", documentation_view.with_ui("swagger")),
    path("api/docs/redoc", documentation_view.with_ui("redoc")),
    path('admin/', admin.site.urls),
    path('', include('citas_veterinaria.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
