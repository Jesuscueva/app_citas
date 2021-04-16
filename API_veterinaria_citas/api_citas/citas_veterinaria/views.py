
# Create your views here.

from .serializers import * 
from .models import * 
from uuid import uuid4

from rest_framework import generics, status
from rest_framework.response import Response

## Agregado por Jesus
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView as SimpleTokenObtainPairView
from .permisions import administradorPost, administradorPut
import os
from django.conf import settings
## Agregado por Jesus


class VeterinariaController(generics.ListCreateAPIView):
    queryset = VeterianriaModel.objects.all()
    serializer_class = VeterinariaSerializer
    permission_classes = [IsAuthenticated]

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
    # Agregado por Jesus
    permission_classes = [IsAuthenticated, administradorPut]
    # Agregado por Jesus
    def get_queryset(self, id):
        return VeterianriaModel.objects.filter(veterinariaId=id).first()

    def get(self, request, id):
        veterinaria = self.get_queryset(id)
        respuesta = self.serializer_class(instance=veterinaria)
        if veterinaria:
            return Response({
                "success": True,
                "content": respuesta.data,
                "message": None
            })
        else:
            return Response({
                "success": False,
                "content": None,
                "message": "No se encontro la veterinaria con ID {}".format(id)
            })

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
    # Agregado por Jesus
    permission_classes = [IsAuthenticated, administradorPost]
    # Agregado por Jesus

    # Agregado por Diego -----------------
    def filtrar_veterinarios(self):
        veterinarios = VeterinarioModel.objects.all()
        resultado = []
        for veterinario in veterinarios:
            if (veterinario.veterinarioEstado):
                resultado.append(veterinario)
        return resultado

    def get(self, request):
        respuesta = self.serializer_class(instance=self.filtrar_veterinarios(), many=True)
    # -------------------
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
    # Agregado por Jesus
    permission_classes = [IsAuthenticated, administradorPut]
    # Agregado por Jesus
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
    
    # --------- Agregado por Diego -------------
    # Eliminar (DELETE) para los veterinarios    
    def delete(self, request, id):
        consulta = self.get_queryset(id)
        imagen = str(consulta.veterinarioFoto)
        if consulta: 
            print(consulta)
            print(imagen)
            rutaImagen = settings.MEDIA_ROOT / imagen
            os.remove(rutaImagen)
            respuesta = self.serializer_class(instance=consulta)
            respuesta.delete()   
            return Response(data={
                "success": True,
                "content": None,
                "message": "Se inhabilito al veterinario exitosamente"
            })
        else:
            return Response(data={
                "success": False,
                "content": None,
                "message": "El veterinario no existe"
            })
    

class serviciosController(generics.ListCreateAPIView):
    queryset = ServicioModel.objects.all()
    serializer_class = ServiciosSerializer
    # Agregado por Jesus
    permission_classes = [IsAuthenticated, administradorPost]
    # Agregado por Jesus

    # Agregado por Diego --------------
    def filtrar_servicios(self):
        servicios = ServicioModel.objects.all()
        resultado = []
        for servicio in servicios:
            if (servicio.servicioEstado):
                resultado.append(servicio)
        return resultado
    
    def get(self, request):
        respuesta = self.serializer_class(instance=self.filtrar_servicios(), many= True)
    # ------------------
        return Response({
            "success": True,
            "content": respuesta.data,
            "message": None
        })
    def post(self, request):
        respuesta = self.serializer_class(data=request.data)
        if respuesta.is_valid():
            respuesta.save()
            return Response({
                "success": True,
                "content": respuesta.data,
                "message": "Creado con exito"
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                "success": False,
                "content": respuesta.errors,
                "message": "Servicio no se creo correctamente"
            })

# ----------------- Agregado por Diego -------------------
# Actualizar (PUT) y Eliminar (DELETE) Servicios
class ServicioController(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicioModel.objects.all()
    serializer_class = ServiciosSerializer

    def get_queryset(self, id):
        return ServicioModel.objects.filter(servicioId=id).first()

    def get(self, request, id):
        servicio = self.get_queryset(id)
        respuesta = self.serializer_class(instance=servicio)
        if servicio:
            return Response(data={
                "success": True,
                "content": respuesta.data,
                "message": None
            })
        else:
            return Response(data={
                "success": True,
                "content": None,
                "message": "No se encontro el servicio con ID {}".format(id)
            })

    def put(self, request, id):
        servicio = self.get_queryset(id)
        respuesta = self.serializer_class(instance=servicio, data=request.data)
    
        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response(data={
                "success": True,
                "content": resultado,
                "message": "Se actualizo el servicio exitosamente"
            })
        else: 
            return Response(data={
                "success": False,
                "content": respuesta.errors,
                "message": "Data incorrecta"
            })


    def delete(self, request, id):
        consulta = self.get_queryset(id)
        imagen = str(consulta.servicioFoto)
        if consulta: 
            respuesta = self.serializer_class(instance=consulta)
            rutaIMG= settings.MEDIA_ROOT / imagen
            os.remove(rutaIMG)
            respuesta.deleted()
            return Response(data={
                "success": True,
                "content": None,
                "message": "Se inhabilito el servicio exitosamente"
            })
        else:
            return Response(data={
                "success": False,
                "content": None,
                "message": "Servicio no existe"
            })

# -----------------------------------------------


# Registrar Usuarios
class RegistroUsuariosController(generics.CreateAPIView):
    serializer_class = RegistroUsuariosSerializer

    def post(self, request):
        print(request.FILES)
        formato = request.FILES['usuarioFoto'].name.split('.')[1]
        print(formato)
        nombre=str(uuid4())+'.'+formato
        request.FILES['usuarioFoto'].name = nombre
        nuevoUsuario = self.serializer_class(data=request.data)
        if nuevoUsuario.is_valid():
            nuevoUsuario.save()
            return Response({
                "succes": True,
                "content": nuevoUsuario.data,
                "message": None
            }, status.HTTP_201_CREATED)
        else:
            return Response({
                "success": True,
                "content": nuevoUsuario.errors,
                "message": "Error al crear nuevo usuario"
            }, status.HTTP_400_BAD_REQUEST)

#Agregado por Jesus
class CustomPayloadController(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomPayloadSerializer

class MascotasController(generics.ListCreateAPIView):
    queryset = MascotaModel.objects.all()
    serializer_class = MascotarSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        respuesta = self.serializer_class(instance = self.get_queryset(), many=True)
        return Response({
            "success": True,
            "content": respuesta.data,
            "message": None
        })
    def post(self, request):
        respuesta = self.serializer_class(data=request.data)
        if respuesta.is_valid():
            respuesta.save()
            return Response({
                "success": True,
                "content": respuesta.data,
                "message": "Mascota registrada con exito"
            }, status.HTTP_201_CREATED)
        else: 
            return Response({
                "success": False,
                "content": respuesta.errors,
                "message": "Error al crear mascota"
            },status.HTTP_400_BAD_REQUEST)


class MascotaDelUsuarioPorId(generics.ListAPIView):
    queryset = UsuarioModel.objects.all()
    serializer_class = MascotaUsuarioSerializer    
    
    def get_queryset(self, id):
        return UsuarioModel.objects.filter(usuarioId=id).first()

    def get(self, request, id):
        respuesta = self.serializer_class(instance= self.get_queryset(id))
        return Response({
            "success": True,
            "content": respuesta.data,
            "message": None
        })


# Agregado por Diego
# PUT y DELETE para la Mascota, completados
class MascotaController(generics.RetrieveUpdateDestroyAPIView):
    queryset = MascotaModel.objects.all()
    serializer_class = MascotasSerializer

    def get_queryset(self, id):     
        return MascotaModel.objects.filter(mascotaId=id).first()

    # def get(self, request, id):
    #     mascota = self.get_queryset(id)
    #     respuesta = self.serializer_class(instance=mascota)
    #     if mascota: 
    #         return Response(data={
    #             "success": True,
    #             "content": respuesta.data,
    #             "message": None
    #         })
    #     else: 
    #         return Response(data={
    #             "success": True,
    #             "content": None,
    #             "message": "No se encontró la mascota"  
    #         })
        
    def put(self, request, id):
        mascota = self.get_queryset(id)
        respuesta = self.serializer_class(instance=mascota, data=request.data)     

        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response(data={
                "success": True,
                "content": resultado.data,
                "message":"Se actualizó la mascota"
            })
        else: 
            return Response(data={
                "success": False,
                "content": respuesta.errors,
                "message": "Data incorrecta"
            }, status=400)

    def delete(self, request, id):
        consulta = self.get_queryset(id)
        if consulta: 
            respuesta = self.serializer_class(instance=consulta) 
            respuesta.delete()
            return Response(data={
                "success": True,
                "content": None,
                "message": "Se inhabilitó la mascota exitosamente"
            })
        else:  
            return Response(data={
                "success": False,
                "content": None,
                "message": "La mascota no existe"
            
            })

class CitasController(generics.ListCreateAPIView):
    queryset = CitaModel.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [IsAuthenticated]

    def filtrar_citas(self):
        citas = CitaModel.objects.all()
        resultado = []
        for cita in citas:
            if (cita.citaEstado):
                resultado.append(cita)
        return resultado

    def get(self, request):
        respuesta = self.serializer_class(instance=self.filtrar_citas(), many=True)
        return Response(data={
            "success": True,
            "content": respuesta.data,
            "message": None
        })

    def post(self, request):
        respuesta = self.serializer_class(data=request.data)
        if respuesta.is_valid():
            respuesta.save()
            return Response(data={
                "success": True,
                "content": respuesta.data,
                "message": "Cita creada con éxito"
            }, status=201)
        else:
            return Response(data={
                "success": False,
                "content": respuesta.errors,
                "message": "Servicio no se creo correctamente"
            })

class CitaController(generics.RetrieveUpdateDestroyAPIView):
    queryset= CitaModel.objects.all()
    serializer_class = CitaSerializer

    def get_queryset(self, id):
        return CitaModel.objects.filter(citaId=id).first()

    def get(self, request, id):
        cita = self.get_queryset(id)
        respuesta = self.serializer_class(instance=cita)
        if cita:
            return Response(data={
                "success": True,
                "content": respuesta.data,
                "message": None
            })
        else:
            return Response(data={
                "success": True,
                "content": None,
                "message": "No se encontró el servicio con ID {}".format(id)
            })

    def put(self, request, id):
        cita = self.get_queryset(id)
        respuesta = self.serializer_class(instance=cita, data=request.data)

        if respuesta.is_valid():
            resultado = respuesta.update()
            return Response(data={
                "success": True,
                "content": resultado,
                "message": "Se ha actualizado la cita exitosamente"
            })
        else:
            return Response(data={
                "success": False,
                "content": respuesta.errors,
                "message": "Data incorrecta"
            })

    def delete(self, request, id):
        consulta = self.get_queryset(id)
        if consulta: 
            respuesta = self.serializer_class(instance=consulta) 
            respuesta.delete()
            return Response(data={
                "success": True,
                "content": None,
                "message": "Se inhabilitó la cita exitosamente"
            })
        else:  
            return Response(data={
                "success": False,
                "content": None,
                "message": "La cita no existe"
            
            })


