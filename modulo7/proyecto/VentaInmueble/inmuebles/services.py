import django
import sys
import os
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


def consulta_inmuebles_comuna(comuna):

    select = f"""
        SELECT i.id_inmueble, i.nombre, i.descripcion, c.nombre_comuna
        FROM inmuebles_inmueble i
        JOIN inmuebles_comuna c ON i.id_comuna_id = c.id_comuna
        WHERE c.nombre_comuna like '{comuna}'
        ORDER BY c.nombre_comuna ASC
    """
    inmuebles = Inmueble.objects.raw(select)

    with open('inmuebles_por_comuna.txt', 'w', encoding='utf-8') as file:
        current_comuna = None
        for inmueble in inmuebles:
            if current_comuna != inmueble.nombre_comuna:
                current_comuna = inmueble.nombre_comuna
                file.write(f'\nComuna: {current_comuna}\n')
                file.write('====================\n')
            file.write(f'Nombre: {inmueble.nombre}\n')
            file.write(f'Descripción: {inmueble.descripcion}\n\n')


if __name__ == "__main__":
    consulta_inmuebles_comuna()


def consulta_inmuebles_region(region):

    select = f"""
        SELECT i.id_inmueble, i.nombre, i.descripcion, r.nombre_region
        FROM inmuebles_inmueble i
        JOIN inmuebles_region r ON i.id_region_id = r.id_region
        WHERE r.nombre_region like '{region}'
        ORDER BY r.nombre_region ASC
    """

    inmuebles = Inmueble.objects.raw(select)

    with open('inmuebles_por_region.txt', 'w', encoding='utf-8') as file:
        current_region = None
        for inmueble in inmuebles:
            if current_region != inmueble.nombre_region:
                current_region = inmueble.nombre_region
                file.write(f'\nRegión: {current_region}\n')
                file.write('====================\n')
            file.write(f'Nombre: {inmueble.nombre}\n')
            file.write(f'Descripción: {inmueble.descripcion}\n\n')


if __name__ == "__main__":
    consulta_inmuebles_region()
