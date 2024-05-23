from .models import Curso, Estudiante, Profesor, Direccion

"""
Estos servicios son:
● crear_curso *
● crear_profesor *
● crear_estudiante *
● crear_direccion *
● obtiene_estudiante *
● obtiene_profesor *
● obtiene_curso *
● agrega_profesor_a_curso
● agrega_cursos_a_estudiante
● imprime_estudiante_cursos

"""


def crear_curso(codigo, nombre, version):
    curso = Curso(codigo=codigo, nombre=nombre, version=version)
    curso.save()
    return curso


def crear_profesor(rut, nombre, apellido, activo, creado_por):
    profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido,
                        activo=activo, creado_por=creado_por)
    profesor.save()
    return profesor


def crear_estudiante(rut, nombre, apellido, fecha_nac, activo, creado_por):
    estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido,
                            fecha_nac=fecha_nac, activo=activo, creado_por=creado_por)
    estudiante.save()
    return estudiante


def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante_id):
    estudiante = obtiene_estudiante(estudiante_id)
    direccion = Direccion(calle=calle, numero=numero, dpto=dpto, comuna=comuna,
                          ciudad=ciudad, region=region, estudiante_id=estudiante)
    direccion.save()
    return direccion


def obtiene_estudiante(rut):
    return Estudiante.objects.get(rut=rut)


def obtiene_profesor(rut):
    return Profesor.objects.get(rut=rut)


def obtiene_curso(codigo):
    return Curso.objects.get(codigo=codigo)


def agrega_profesor_a_curso(rut, codigo):
    profesor = Profesor.objects.get(rut=rut)
    curso_id = Curso.objects.get(codigo=codigo)
    profesor.curso.add(curso_id)


def agrega_cursos_a_estudiante(rut, codigo):
    estudiante = Estudiante.objects.get(rut=rut)
    curso_id = Curso.objects.get(codigo=codigo)
    estudiante.curso.add(curso_id)


def imprime_estudiante_cursos(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    cursos = estudiante.curso.all()
    print(f"Estudiante: {estudiante.nombre} {estudiante.apellido}")
    print("Cursos:")
    for curso in cursos:
        print(f"- {curso.nombre} (Versión {curso.version})")
