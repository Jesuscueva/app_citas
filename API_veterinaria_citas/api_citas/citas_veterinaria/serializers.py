
from re import S
from django.db.models import fields
from .models import * 
from rest_framework import serializers


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

    # veterinaria = VeterinariaSerializer(source= 'veterinaria', many=True)
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
    class Meta:
        model = VeterinarioModel
        # fields = ['veterinarioNombre', 'veterinarioApellido', 'veterinarioDescripcion', 'veterinarioFoto']
        fields = '__all__'

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioModel
        fields = "__all__"
    

class RegistroUsuariosSerializer(serializers.ModelSerializer):

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

class MascotarSerializer(serializers.ModelSerializer):

    class Meta:
        model= MascotaModel
        fields = "__all__"