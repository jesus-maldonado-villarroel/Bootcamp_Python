from django.db import models
from django.contrib.auth.models import User


class Inmueble(models.Model):

    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=False, blank=False)
    m2_contruidos = models.FloatField(null=False, blank=False)
    m2_totales = models.FloatField(null=False, blank=False)
    cantidad_estacionamientos = models.IntegerField(null=False, blank=False)
    cantidad_habitaciones = models.IntegerField(null=False, blank=False)
    cantidad_baños = models.IntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=250, null=False, blank=False)
    id_comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE)
    tipo_inmueble = models.CharField(max_length=20, choices=[(
        'casa', 'Casa'), ('departamento', 'Departamento'), ('parcela', 'Parcela')])
    precio_mensual = models.FloatField(null=False, blank=False)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f" nombre inmueble: {self.nombre}"


class Perfil(models.Model):

    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, null=False, blank=False)
    direccion = models.CharField(max_length=250, null=False, blank=False)
    telefono = models.CharField(max_length=9, null=False, blank=False)
    email = models.EmailField(
        max_length=250, unique=True, null=False, blank=False)
    tipo_usuario = models.CharField(choices=[(
        'arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador',)])

    def __str__(self):
        return self.usuario.username


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_comuna


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_region


class Contact(models.Model):
    arrendador = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre_inmueble = models.CharField()
    correo = models.EmailField()
    celular = models.CharField(max_length=10)
    name = models.CharField(max_length=64)
    mensaje = models.TextField()
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.correo} - Mensaje: {self.mensaje}"
