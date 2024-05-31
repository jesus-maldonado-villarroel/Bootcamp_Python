from .models import User
from .models import User, Inmueble, Comuna, Region, Usuario


def crear_usuario():
    pass


def crear_user():
    pass


def crear_inmueble():
    pass


def consulta_inmuebles_comuna(comuna):

    select = f"""
        SELECT i.id, i.nombre, i.descripcion, c.nombre_comuna
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
        SELECT i.id, i.nombre, i.descripcion, r.nombre_region
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
