from django.contrib import admin
from .models import Estudiante, Curso, Profesor, Direccion
# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Direccion)
