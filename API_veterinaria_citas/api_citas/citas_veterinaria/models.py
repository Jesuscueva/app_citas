
from re import T
from django import db
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.db.models.base import 
from .authmanager import UsuariosManager

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    TIPO_PERSONAL = [
        (1, 'ADMINISTRADOR'),
        (2, 'CLIENTE')
    ]
    usuarioId= models.AutoField(
        primary_key= True,
        unique=True,
        db_column= "usuario_id",
    )
    usuarioNombre = models.CharField(
        db_column= "usuario_nombre",
        max_length= 45,
        verbose_name= "Nombre del usuario",
        null=False
    )
    usuarioApellido = models.CharField(
        db_column= "usuario_apellido",
        max_length= 45,
        null=False,
        verbose_name= "Apellido del usuario"
    )
    usuarioEmail = models.EmailField(
        max_length= 30,
        db_column= "usuario_email",
        verbose_name="Correo del usuario",
        unique= True
    )
    usuarioTipo= models.IntegerField(
        db_column="usuario_tipo",
        verbose_name= "Tipo de usuario",
        choices= TIPO_PERSONAL
    )
    password = models.TextField(
        db_column='usuario_password',
        verbose_name='Contraseña del Usuario'
    )
    usuarioCelular = models.CharField(
        max_length= 20,
        db_column= "usuario_telefono",
        verbose_name= "Telefono del usuario",
        null=True
    )
    usuarioFoto = models.ImageField(
        upload_to = "usuario/",
        db_column = "usuario_foto",
        verbose_name= "Foto del usuario",
        default="default.png",
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UsuariosManager()

    USERNAME_FIELD = "usuarioEmail"

    REQUIRED_FIELDS = ["usuarioNombre", "usuarioApellido", "usuarioTipo"]

    class Meta:
        db_table = "t_usuarios"
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"


class VeterianriaModel(models.Model):
    veterinariaId = models.AutoField(
        primary_key= True,
        unique=True,
        db_column= "veterinaria_id"
    )
    veterinariaNombre = models.CharField(
        max_length= 45,
        null= False,
        db_column= "veterinaria_nombre",
        verbose_name= "Nombre de la veterinaria"
    )
    veterinariaLogo = models.ImageField(
        upload_to = "veterinaria/",
        db_column = "veterinaria_logo",
        verbose_name= "Logo de la veterinaria",
        null = False
    )
    veterinariaDescripcion = models.TextField(
        db_column= "veterinaria_descripcion",
        verbose_name= "Descripcion de la veterinaria",
        null= False
    )
    veterinariaTelefono = models.CharField(
        max_length= 15,
        db_column= "veterinaria_telefono",
        verbose_name= "Telefono de la Empresa",
        null=False
    )
    veterinariaDireccion = models.TextField(
        db_column= "veterinaria_direccion",
        verbose_name= "Direccion de la veterinaria"
    )
    veterinariaHorario = models.TextField(
        db_column= "veterinaria_horario",
        verbose_name="Horario de la veterinaria"
    )
    veterinariaCorreo = models.TextField(
        db_column= "veterinaria_correo",
        verbose_name= "veterinaria correo"
    ) 
    

    class Meta: 
        db_table = "t_veterinaria"
        verbose_name = "Veterinaria"


class VeterinarioModel(models.Model):
    veterinarioId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column= "veterinario_id"
    )
    veterinarioNombre = models.CharField(
        max_length= 45,
        db_column= "veterinario_nombre",
        null=False,
        verbose_name= "Nombre de la veterinario"
    )
    veterinarioApellido = models.CharField(
        max_length= 45,
        db_column= "veterinario_apellido",
        null=False,
        verbose_name= "Apellido de la veterinario"
    )
    veterinarioDescripcion = models.TextField(
        db_column= "veterinario_descripcion",
        verbose_name= "Descripcion del veterinario"
    )
    veterinarioFoto = models.ImageField(
        upload_to = "veterinario/",
        db_column= "veterinaria_foto",
        verbose_name= "Foto del veterinario",
        null= True 
        )
    veterinarioEstado = models.BooleanField(
        default=True,
        db_column="especie_estado",
        null=False
    )

    veterinaria = models.ForeignKey(
        to = VeterianriaModel,
        related_name= "veterinariosVeterinaria",
        db_column= "veterinaria_id",
        on_delete= models.PROTECT,
        null=True
    )

    class Meta:
        db_table = "t_veterinario"
        verbose_name = "veterinario"

class ServicioModel(models.Model):
    servicioId = models.AutoField(
        primary_key= True,
        null=False,
        unique=True,
        db_column= "servicio_id"
    )
    servicioNombre= models.CharField(
        db_column= "servicio_nombre",
        null= False,
        verbose_name= "Nombre del servicio",
        max_length= 45
    )
    servicioDescripcion = models.TextField(
        db_column= "servicio_descripcion",
        verbose_name= "Descripcion del servicio"
    )
    servicioFoto = models.ImageField(
        upload_to = "servicio/",
        db_column = "servicio_foto",
        null= True,
        verbose_name= "Foto del Servicio"
    )
    servicioEstado = models.BooleanField(
        default=True,
        db_column="servicio_estado",
        null=False
    )
    veterinaria = models.ForeignKey(
        db_column= "veterinaria_id",
        to= VeterianriaModel,
        related_name= "servicioVeterinaria",
        on_delete= models.PROTECT,
        null=True
    )
    class Meta:
        db_table = "t_servicio"
        verbose_name = "servicio"


class SedeModel(models.Model):
    sedeId = models.AutoField(
        primary_key= True,
        unique=True,
        null=False,
        db_column= "sede_id"
    )

    sedeDireccion = models.TextField(
        db_column= "sede_direccion",
        null=False,
        verbose_name= "Direccion de la empresa"
    )

    veterinaria = models.ForeignKey(
        db_column= "veterinaria_id",
        to= VeterianriaModel,
        related_name= "veterinariaSede",
        on_delete= models.CASCADE,
        null= True
    )
    class Meta:
        db_table = "t_sede"
        verbose_name = "sede"

class CitaModel(models.Model):
    ESTADO = [
        (1, "PENDIENTE"),
        (2, "ECHO"),
        (2, "CANCELADO")
    ]
    citaId = models.AutoField(
        db_column= "cita_id",
        primary_key=True,
        null=False,
        unique=True,
    )
    citaFecha = models.DateField(
        db_column= "cita_fecha",
        verbose_name= "Fecha de la cita"
    )
    citaCosto = models.DecimalField(
        db_column= "cita_costo",
        verbose_name= "Costo de la cita",
        max_digits= 6,
        decimal_places= 3,
        null=False
    )
    citaEstado= models.IntegerField(
        db_column= "cita_estado",
        verbose_name= "Estado de la cita",
        choices= ESTADO
    )
    veterinaria = models.ForeignKey(
        to= VeterianriaModel,
        db_column= "veterinaria_id",
        on_delete= models.CASCADE,
        related_name= "veterinariaCita"
    )
    cliente = models.ForeignKey(
        to= UsuarioModel,
        related_name="cliente",
        db_column="usuario",
        on_delete= models.CASCADE,
        null=True
    )
    sede = models.ForeignKey(
        to= SedeModel,
        db_column= "sede_id",
        on_delete= models.CASCADE,
        related_name= "sede",
        null= True
    )
    servicio = models.ForeignKey(
        to= ServicioModel,
        related_name= "servicio",
        on_delete= models.CASCADE,
        db_column= "servicio_id",
        null= True
    )
    class Meta: 
        db_table = "t_cita"
        verbose_name = "cita"

class MascotaModel(models.Model):
    mascotaId = models.AutoField(
        primary_key=True,
        unique= True,
        null=False,
        db_column= "mascota_id"
    )
    mascotaNombre = models.CharField(
        null=False,
        verbose_name= "Nombre de la Mascota",
        db_column= "mascota_nombre",
        max_length= 55,
        unique=True
    )
    mascotaEdad = models.IntegerField(
        null=False,
        verbose_name= "Edad de la Mascota",
        db_column= "mascota_edad"
    )
    mascotaFoto = models.ImageField(
        upload_to = "mascota/",
        db_column = "mascota_foto",
        null= True,
        verbose_name= "Foto de la mascota"
    )
    mascotaEstado = models.BooleanField(
        default=True,
        db_column="mascota_estado",
        null=False
    )
    cliente = models.ForeignKey(
        to=UsuarioModel,
        db_column= "usuario",
        verbose_name="Usuario de la Mascota",
        on_delete= models.PROTECT,
        related_name= "mascotaUsuario",
        null=True
    )

    class Meta:
        db_table = "t_mascota"
        verbose_name = "mascota"
