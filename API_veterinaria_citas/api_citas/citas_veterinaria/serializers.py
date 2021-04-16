
from re import S, search
from django.db.models import fields
from rest_framework_simplejwt import tokens
from .models import * 
from rest_framework import serializers

# Agregado por Jesus
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as SimpleTokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _

class VeterinariaSerializer(serializers.ModelSerializer):

    

    def update(self):
        self.instance.veterinariaNombre = self.validated_data.get('veterinariaNombre')
        self.instance.veterinariaLogo = self.validated_data.get('veterinariaLogo')
        self.instance.veterinariaDescripcion = self.validated_data.get('veterinariaDescripcion')
        self.instance.veterinariaTelefono = self.validated_data.get('veterinariaTelefono')
        self.instance.veterinariaDireccion = self.validated_data.get('veterinariaDireccion')
        self.instance.save()
        return self.data

    class Meta: 
        model = VeterianriaModel
        fields = "__all__"

class VeterinarioSerializer(serializers.ModelSerializer):
    # veterinaria = VeterinariaSerializer()

    # veterinaria = VeterinariaSerializer(source= 'veterinaria_id', many=True)
    def update(self):
        self.instance.veterinarioNombre = self.validated_data.get('veterinarioNombre')
        self.instance.veterinarioApellido = self.validated_data.get('veterinarioApellido')
        self.instance.veterinarioFoto = self.validated_data.get('veterinarioApellido')
        self.instance.veterinarioDescripcion =self.validated_data.get('veterinarioDescripcion')
        
        self.instance.save()
        return self.data

    # def delete(self):
    #     print(self.instance)

    #     if(self.instance):
    #         self.instance

    # ------ Agregado por Diego ------------
    def delete(self):
        self.instance.veterinarioEstado = False
        self.instance.save()
        return self.instance
    # ---------------------------------

    class Meta:
        model = VeterinarioModel
        fields = '__all__'

class ServiciosSerializer(serializers.ModelSerializer):
    # veterinaria = VeterinariaSerializer()
    def update(self):
        self.instance.servicioNombre = self.validated_data.get('servicioNombre')
        self.instance.servicioDescripcion = self.validated_data.get('servicioDescripcion')
        self.instance.servicioFoto = self.validated_data.get('servicioFoto')
        self.instance.veterinaria  = self.validated_data.get('veterinaria')
        self.instance.save()

    def deleted(self):
        self.instance.servicioEstado = False
        self.instance.save()
        return self.instance

    class Meta:
        model = ServicioModel
        fields = "__all__"
    
class UsuarioSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    # print(password)

    def save(self):
        usuarioNombre = self.validated_data.get('usuarioNombre')
        usuarioApellido = self.validated_data.get('usuarioApellido')
        usuarioEmail = self.validated_data.get('usuarioEmail')
        usuarioTipo = self.validated_data.get('usuarioTipo')
        password = self.validated_data.get('password')
        usuarioCelular = self.validated_data.get('usuarioCelular')
        usuarioFoto = self.validated_data.get('usuarioFoto')
        is_staff = False
        nuevoUsuario = UsuarioModel(
            usuarioNombre = usuarioNombre,
            usuarioApellido = usuarioApellido,
            usuarioEmail = usuarioEmail,
            usuarioTipo = usuarioTipo,
            usuarioCelular = usuarioCelular,
            usuarioFoto = usuarioFoto,
            is_staff = is_staff
        )

        nuevoUsuario.set_password(password)
        print("assss")
        print(nuevoUsuario.password)
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta: 
        model = UsuarioModel
        exclude = ['groups', 'user_permissions']

class MascotasSerializer(serializers.ModelSerializer):

    def update(self):
        self.instance.mascotaNombre = self.validated_data.get("mascotaNombre")
        self.instance.mascotaEdad = self.validated_data.get("mascotaEdad")
        self.instance.cliente = self.validated_data.get("cliente")
        self.instance.save()
        return self

    def delete(self):
        self.instance.mascotaEstado = False
        self.instance.save()
        return self.instance
    
    class Meta:
        model= MascotaModel
        fields = "__all__"

#Agregado por Jesus
class RegistroUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = ["usuarioNombre", "usuarioApellido", "usuarioCelular", "usuarioFoto"]

class MascotarSerializer(serializers.ModelSerializer):
    class Meta:
        model= MascotaModel
        fields = "__all__"

class MascotaUsuarioSerializer(serializers.ModelSerializer):
    mascota = MascotarSerializer(source="mascotaUsuario", many=True, read_only=True)
    class Meta:
        model = UsuarioModel
        exclude = ["last_login","is_superuser","usuarioTipo","password",   "is_active", "is_staff", "groups", "user_permissions"]

class CustomPayloadSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token =  super(CustomPayloadSerializer, cls).get_token(user)
        token['usuarioTipo'] = user.usuarioTipo
        token['usuarioNombre'] = user.usuarioNombre
        token['usuarioApellido'] = user.usuarioApellido
        print(user)
        print(token)
        return token

class CitaSerializer(serializers.ModelSerializer):
    def update(self):
        self.instance.citaFecha = self.validated_data.get("citaFecha")
        self.instance.citaCosto = self.validated_data.get("citaCosto")
        self.instance.citaEstado = self.validated_data.get("citaEstado")
        self.instance.servicio = self.validated_data.get("servicio")

    def delete(self):
        self.instance.citaEstado = False
        self.instance.save()
        return self.instance

    class Meta:
        model = MascotaModel
        fields = "__all__"

#Agregado por Jesus 