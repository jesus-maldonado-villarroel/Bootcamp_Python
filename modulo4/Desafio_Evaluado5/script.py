import json
from usuario import Usuario


def crear_instancia_usuario(linea):
    try:
        datos_usuario = json.loads(linea)
        usuario = Usuario(datos_usuario["nombre"], datos_usuario["apellido"],
                          datos_usuario["email"], datos_usuario["genero"])
        return usuario

    except Exception as e:
        with open("error.log", "a") as log_error:
            log_error.write(
                f"Se encuentra un error en la siguiente linea: {linea}\n")
            log_error.write(f"Mensaje de error: {(e)}\n\n")
            return None


usuarios = []
with open("usuarios.txt", "r") as archivo_usuarios:
    for linea in archivo_usuarios:
        usuario = crear_instancia_usuario(linea)
        if usuario:
            usuarios.append(usuario)
