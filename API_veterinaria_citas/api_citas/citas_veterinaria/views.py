
# Create your views here.

from django import conf
from .serializers import * 
from .models import * 
from uuid import uuid4

from rest_framework import generics, status
from rest_framework.response import Response


class VeterinariaController(generics.ListCreateAPIView):
    queryset = VeterianriaModel.objects.all()
    serializer_class = VeterinariaSerializer

    def get(self, request):
        respuesta = self.serializer_class(
            instance= self.get_queryset(), many=True
        )

        return Response({
            "success": True,
            "content": respuesta.data,
            "message": None
        })

    def post(self, request):
        print(request.FILES)
        formato = request.FILES['veterinariaLogo'].name.split('.')[1]
        nombre=str(uuid4())+'.'+formato
        request.FILES['veterinariaLogo'].name = nombre
        respuesta =self.serializer_class(data=request.data)
        if respuesta.is_valid():
            respuesta.save()
            return Response({
                "success": True,
                "content": respuesta.data,
                "message": "creado con exito"
            })
        else: 
            return Response({
                "succes": False,
                "content": respuesta.errors,
                "message": "error al crear"
            }, status.HTTP_400_BAD_REQUEST)

class ActualizarVeterinariaController(generics.RetrieveUpdateDestroyAPIView):
    queryset = VeterianriaModel.objects.all()
    serializer_class = VeterinariaSerializer

    def get_queryset(self, id):
        return VeterianriaModel.objects.filter(veterinariaId=id).first()

    def put(self, request, id):
        veterinaria = self.get_queryset(id)
        print(id)
        print(veterinaria)
        print(request)
        formato = request.FILES['veterinariaLogo'].name.split('.')[1]
        nombre=str(uuid4())+'.'+formato
        request.FILES['veterinariaLogo'].name = nombre
        respuesta = self.serializer_class(instance=veterinaria, data=request.data)
        if respuesta.is_valid():
            return Response({
                "success": True,
                "content": respuesta.update(),
                "message": "Veterinaria Actualizada correctamente"
            })
        else:
            return Response({
                "success": False,
                "content": respuesta.errors,
                "message": "Data incorrecta"
            }, status.HTTP_400_BAD_REQUEST)


class VeterinariosController(generics.ListCreateAPIView): 
    queryset = VeterinarioModel.objects.all()
    serializer_class = VeterinarioSerializer
    
    def get(self, request):
        respuesta = self.serializer_class(instance= self.get_queryset(), many=True)

        return Response({
            "success": True,
            "content": respuesta.data,
            "message": None
        })

    def post(self, request):
        formato = request.FILES['veterinarioFoto'].name.split('.')[1]
        print(formato)
        nombre = str(uuid4())+'.'+formato
        request.FILES['veterinarioFoto'].name = nombre
        respuesta =self.serializer_class(data=request.data)
        if respuesta.is_valid():
            respuesta.save()
            return Response({
                "success": True,
                "content": respuesta.data,
                "message": "Veterinario creado exitosamente"
            })
        else:
            return Response({
                "success": False,
                "content": respuesta.errors,
                "message": "Error al crear"
            }, status.HTTP_400_BAD_REQUEST)

class veterinarioController(generics.RetrieveUpdateDestroyAPIView):
    queryset = VeterinarioModel.objects.all()
    serializer_class = VeterinarioSerializer

    def get_queryset(self, id):
        return VeterinarioModel.objects.filter(veterinarioId=id).first()

    def get(self, request, id):
        veterinario = self.get_queryset(id)
        respuesta = self.serializer_class(instance=veterinario)
        if respuesta:
            return Response({
                "success": True,
                "content": respuesta.data,
                "message": None
            })
        else:
            return Response({
                "success": False,
                "content": None,
                "message": "No se encontro el veterinario con ID {}".format(id)
            })
    
    def put(self, request, id):
        veterinario = self.get_queryset(id)
        formato = request.FILES['veterinarioFoto'].name.split('.')[1]
        nombre = str(uuid4())+'.'+formato
        request.FILES['veterinarioFoto'].name = nombre
        respuesta = self.serializer_class(instance=veterinario, data=request.data)

        if respuesta.is_valid():
            return Response({
                "success": True,
                "content": respuesta.update(),
                "message": "Veterinario actualizado correctamente"
            })
        else:
            return Response({
                "success": False,
                "content": respuesta.errors,
                "message": "Error al actualizar el veterinario"
            })
    
    def delete(self, request, id):
        pass
    
    #No se puede agregar un veterinario porque me pide veterinaria_id la foreinkey

