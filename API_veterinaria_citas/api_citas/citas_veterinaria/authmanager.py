from django.contrib.auth.models import BaseUserManager


class UsuariosManager(BaseUserManager):
    
    def create_user(self, nombre, apellido, email, tipo,password=None, celular=None, foto=None):

        if not email:
            raise ValueError("El usuario necesita un correo electronico")
        # para normalizar el correo llevarlo todo a lowercase minuscula todo
        email = self.normalize_email(email)
        # creo el objeto del usuairo con los valores de la tabla
        usuario = self.model(
            usuarioNombre = nombre,
            usuarioApellido = apellido,
            usuarioEmail = email,
            usuarioTipo = tipo,
            password = password,
            usuarioCelular = celular,
            usuarioFoto = foto
        )
        # set_password me ayuda a encriptar la contraseña
        usuario.set_password(password)
        #ahora si guardamos el usuario registrado
        usuario.save(using= self._db)
        return usuario

    def create_superuser(self, usuarioNombre, usuarioApellido, usuarioEmail, usuarioTipo,password):
        """Crea un nuevo superusairo para que pueda accedar al panel administrativo y algunas opciones de mas"""

        usuario =  self.create_user(usuarioNombre, usuarioApellido, usuarioEmail, usuarioTipo, password)

        usuario.is_superuser = True
        usuario.is_staff = True

        usuario.save(using = self._db)