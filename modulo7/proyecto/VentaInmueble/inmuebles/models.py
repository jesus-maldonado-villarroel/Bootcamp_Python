from django.db import models

# Create your models here.


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25, null=False, blank=False)
    apellidos = models.CharField(max_length=25, null=False, blank=False)
    rut = models.CharField(max_length=12, null=False, blank=False)
    direccion = models.CharField(max_length=250, null=False, blank=False)
    telefono = models.CharField(max_length=9, null=False, blank=False)
    email = models.EmailField(
        max_length=250, unique=True, null=False, blank=False)
    tipo_usuario = models.CharField(max_length=20, choices=[(
        'arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador',)])

    def __str__(self):
        return f"{self.rut}: {self.nombres} {self.apellidos} tipo user: {self.tipo_usuario}"


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


class Inmueble(models.Model):
    id_inmueble = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)
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
        return f"""
                {self.nombre}:  
                m2_contruidos: {self.m2_contruidos} cantidad habitaciones: {self.cantidad_habitaciones} cantidad de baños: {self.cantidad_baños}
                estacionamientos: {self.cantidad_estacionamientos} 
                direccion: {self.id_comuna} {self.direccion}
                tipo_vivienda: {self.tipo_inmueble}
                precio_mensual: {self.precio_mensual}
                descripcion: {self.descripcion}
                estado: {self.estado}
"""
