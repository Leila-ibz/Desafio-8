
# Se tuvo en cuenta el desafio 5 para realizar el Desafio 8.
# Para el siguiente programa consideramos que un usuario puede ser de dos tipos:
# -Colaborador : Puede publicar articulos y además comentar.
# -Publico : Solo puede realizar comentarios
# Ahora bien teniendo en cuenta que tanto el articulo y comentario precisa un id_usuario 
# Debemos registrarnos primero .
# Teniendo en cuenta esto primero registrese :)

import re
from datetime import datetime

class Usuario:
    id_counter = 1

    def __init__(self, nombre, apellido, telefono, username, email, contraseña):
        self.id = Usuario.id_counter
        Usuario.id_counter += 1
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = datetime.now()
        self.avatar = 'default_avatar.png'
        self.estado = 'offline'

    def login(self):
        # Codigo para el inicio de sesión
        self.estado = 'online'
        print(f"Bienvenidx, {self.username}!")

    def mostrar_menu(self):
        pass  # Método abstracto, se implementa en las subclases

class Publico(Usuario):
    def __init__(self, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(nombre, apellido, telefono, username, email, contraseña)
        self.es_publico = True

    def comentar(self, articulo, comentario):
        # Codigo para el comentario de usuario rol público
        if articulo.estado == 'activo':
            comentario_obj = Comentario(articulo.id, self.id, comentario)
            print(f"{self.username}: \"{comentario_obj.contenido}\"")
        else:
            print("No se puede comentar en un artículo inactivo.")

    def mostrar_menu(self):
        while True:
            print("Acciones disponibles:")
            print("1. Comentar un artículo")
            print("2. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                articulo_id = input("Ingresa el ID del artículo en el que deseas comentar: ")
                comentario = input("Escribe tu comentario: ")
                articulo_encontrado = False

                for articulo in articulos:
                    if str(articulo.id) == articulo_id:
                        articulo_encontrado = True
                        self.comentar(articulo, comentario)
                        break

                if not articulo_encontrado:
                    print("No se encontró el artículo con el ID proporcionado.")

            elif opcion == "2":
                print("¡Adios!, Volvé prontito")
                break

            else:
                print("Opción inválida. Intenta nuevamente.")

class Colaborador(Usuario):
    def __init__(self, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(nombre, apellido, telefono, username, email, contraseña)
        self.es_colaborador = True

    def comentar(self, articulo, comentario):
        # Codigo para el comentario de colaborador
        if articulo.estado == 'activo':
            comentario_obj = Comentario(articulo.id, self.id, comentario)
            print(f"{self.username}: \"{comentario_obj.contenido}\"")
        else:
            print("No se puede comentar en un artículo inactivo.")

    def publicar(self, titulo, resumen, contenido, imagen):
        # Implementación del método de publicación de artículo
        articulo = Articulo(self.id, titulo, resumen, contenido, imagen)
        print(f"El artículo \"{articulo.titulo}\" ha sido publicado con éxito.")
        print(f"Resumen: {articulo.resumen}")
        print(f"Contenido: {articulo.contenido}")
        print(f"Fecha de publicación: {articulo.fecha_publicacion}")
        print(f"Autor: {self.username}")
        print(f"ID de usuario: {self.id}")
        print(f"ID del artículo: {articulo.id}")

        # Agregar el artículo a la lista de artículos
        articulos.append(articulo)

    def mostrar_menu(self):
        while True:
            print("Acciones disponibles:")
            print("1. Comentar un artículo")
            print("2. Publicar un artículo")
            print("3. Ver todos los artículos")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                articulo_id = input("Ingresa el ID del artículo en el que deseas comentar: ")
                comentario = input("Escribe tu comentario: ")
                articulo_encontrado = False

                for articulo in articulos:
                    if str(articulo.id) == articulo_id:
                        articulo_encontrado = True
                        self.comentar(articulo, comentario)
                        break

                if not articulo_encontrado:
                    print("No se encontró el artículo con el ID proporcionado.")

            elif opcion == "2":
                titulo = input("Ingresa el título del artículo: ")
                resumen = input("Ingresa el resumen del artículo: ")
                contenido = input("Ingresa el contenido del artículo: ")
                imagen = input("Ingresa el archivo de la imagen del artículo: ")
                self.publicar(titulo, resumen, contenido, imagen)

            elif opcion == "3":
                print("Artículos:")
                for articulo in articulos:
                    print(f"ID: {articulo.id}")
                    print(f"Título: {articulo.titulo}")
                    print(f"Resumen: {articulo.resumen}")
                    print(f"Contenido: {articulo.contenido}")
                    print("-----")

            elif opcion == "4":
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

class Articulo:
    id_counter = 1

    def __init__(self, id_usuario, titulo, resumen, contenido, imagen):
        self.id = Articulo.id_counter
        Articulo.id_counter += 1
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = datetime.now()
        self.imagen = imagen
        self.estado = 'activo'

class Comentario:
    id_counter = 1

    def __init__(self, id_articulo, id_usuario, contenido):
        self.id = Comentario.id_counter
        Comentario.id_counter += 1
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = datetime.now()
        self.estado = 'activo'

# Registro de usuario
def registrar_usuario():
    nombre = input("Ingresa tu Nombre: ")
    apellido = input("Ingresa tu Apellido: ")
    telefono = input("Ingresa tu Teléfono: ")
    username = input("Ingresa un NickName. por ejemplo “Ana.Gz”: ")
    email = input("Ingresa tu Email: ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("El formato del email es incorrecto.")
        email = input("Email: ")
    contraseña = input("Contraseña: ")

    tipo_usuario = input("Seleccione el tipo de usuario (P: Público, C: Colaborador): ")
    tipo_usuario = tipo_usuario.upper()

    if tipo_usuario == 'P':
        usuario = Publico(nombre, apellido, telefono, username, email, contraseña)
    elif tipo_usuario == 'C':
        usuario = Colaborador(nombre, apellido, telefono, username, email, contraseña)
    else:
        print("Tipo de usuario inválido. Se creará un usuario público por defecto.")
        usuario = Publico(nombre, apellido, telefono, username, email, contraseña)

    usuarios.append(usuario)
    print(f"¡Usuario {usuario.username} registrado con éxito!")

# Lista de usuarios y artículos
usuarios = []
articulos = []

# Menú principal
while True:
    print("Bienvenidx al sistema de blogs:")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Iniciar sesión
        username = input("Ingresa tu NickName: ")
        contraseña = input("Ingresa tu contraseña: ")
        usuario_encontrado = False

        for usuario in usuarios:
            if usuario.username == username and usuario.contraseña == contraseña:
                usuario_encontrado = True
                usuario.login()
                usuario.mostrar_menu()
                break

        if not usuario_encontrado:
            print("Nombre de usuario o contraseña incorrectos.")

    elif opcion == "2":
        # Registrarse
        registrar_usuario()

    elif opcion == "3":
        # Salir
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
