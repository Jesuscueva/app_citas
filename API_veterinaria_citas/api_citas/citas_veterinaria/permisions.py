

from rest_framework.permissions import BasePermission, SAFE_METHODS

class administradorPut(BasePermission):
    def has_permission(self, request, view):
        
        print(request.user.usuarioTipo)

        if request.method == "PUT":
            if request.user.usuarioTipo == 1:
                return True
            else: 
                return False
        else: 
            return True

class administradorPost(BasePermission):
    def has_permission(self, request, view):
        print(request.user.usuarioTipo)
        if request.method == "POST" :
            if request.user.usuarioTipo == 1:
                return True
            else: 
                return False
        else: 
            return True