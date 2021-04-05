
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
        fields = ['veterinarioNombre', 'veterinarioApellido', 'veterinarioDescripcion', 'veterinarioFoto']