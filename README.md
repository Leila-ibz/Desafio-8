# Desafio-8
Desafío 8: Principios de programación orientada a objetos
Clase Usuario
-atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de 
registro, avatar, estado, online
- métodos: login(), registrar()
Clase Publico(Usuario)
- atributo: es_publico
- métodos: registrar(), comentar()
clase Colaborador(Usuario)
- atributos: es_colaborador
- métodos: registrar(), comentar(), publicar()
clase Articulo
- id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado
clase Comentario
- id, id_articulo, id_usuario, contenido, fecha_hora, estadO
