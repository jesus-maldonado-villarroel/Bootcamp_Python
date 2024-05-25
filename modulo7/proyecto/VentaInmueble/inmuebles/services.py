from .models import User
from .models import User, Inmueble, Comuna, Region


def registrar_usuario(nombres, apellidos, rut, direccion, telefono, email, tipo_usuario):

    usuario = User(
        nombres=nombres,
        apellidos=apellidos,
        rut=rut,
        direccion=direccion,
        telefono=telefono,
        email=email,
        tipo_usuario=tipo_usuario
    )
    usuario.save()
    return usuario


def actualizar_usuario(rut, nombres, apellidos, direccion, telefono, email):

    usuario = User.objects.get(rut=rut)

    if nombres:
        usuario.nombres = nombres
    if apellidos:
        usuario.apellidos = apellidos
    if direccion:
        usuario.direccion = direccion
    if telefono:
        usuario.telefono = telefono
    if email:
        usuario.email = email
    usuario.save()
    return usuario


def listar_usuarios():
    usuarios = User.objects.all()
    return usuarios


def listar_inmuebles_por_comuna(nombre_comuna):

    inmuebles = Inmueble.objects.filter(id_comuna__nombre_comuna=nombre_comuna)
    return inmuebles


def publicar_inmueble(rut, nombre, descripcion, m2_contruidos, m2_totales, cantidad_estacionamientos, cantidad_habitaciones, cantidad_baños, direccion, id_comuna, tipo_inmueble, precio_mensual):

    usuario = User.objects.get(rut=rut)
    if usuario.tipo_usuario == 'arrendatario':

        inmueble = Inmueble(
            id_user=usuario,
            nombre=nombre,
            descripcion=descripcion,
            m2_contruidos=m2_contruidos,
            m2_totales=m2_totales,
            cantidad_estacionamientos=cantidad_estacionamientos,
            cantidad_habitaciones=cantidad_habitaciones,
            cantidad_baños=cantidad_baños,
            direccion=direccion,
            id_comuna=Comuna.objects.get(id_comuna=id_comuna),
            tipo_inmueble=tipo_inmueble,
            precio_mensual=precio_mensual
        )
        return inmueble
    else:
        return f"No cumples con los requisitos"


def listar_inmuebles_de_arrendador(rut):
    inmuebles = Inmueble.objects.filter(rut=rut)
    return inmuebles


def eliminar_usuario(rut):
    usuario = User.objects.get(rut=rut)
    usuario.delete()
    return f"El usuario fue eliminado"
