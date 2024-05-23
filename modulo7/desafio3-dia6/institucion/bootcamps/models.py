from django.db import models

# Create your models here.


class Curso(models.Model):
    codigo = models.CharField(
        max_length=10, null=False, blank=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.nombre} Version:{self.version} Codigo:{self.codigo}"


class Estudiante(models.Model):
    rut = models.CharField(max_length=9, null=False,
                           blank=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    curso = models.ManyToManyField(
        'Curso', related_name="Estudiantes")

    def __str__(self):
        cursos = ", ".join([curso.nombre for curso in self.curso.all()])
        return f"{self.nombre} {self.apellido} - Cursos: {cursos}"


class Profesor(models.Model):
    rut = models.CharField(max_length=9, null=False,
                           blank=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    curso = models.ManyToManyField(
        'Curso', related_name="Profesores")

    def __str__(self):
        cursos = ", ".join([curso.nombre for curso in self.curso.all()])
        return f"{self.nombre} {self.apellido} - Cursos: {cursos}"


class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    dpto = models.CharField(max_length=10, null=False, blank=False)
    comuna = models.CharField(max_length=10, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    estudiante_id = models.OneToOneField(
        'Estudiante', on_delete=models.CASCADE, unique=True, null=False)

    def __str__(self):
        return f"{self.estudiante_id.nombre} {self.estudiante_id.apellido} - Dirección: {self.calle} {self.numero}, {self.dpto}, {self.comuna}, {self.ciudad}, {self.region}"
