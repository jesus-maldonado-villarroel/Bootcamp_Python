from django.contrib import admin
from .models import Perfil, Inmueble, Comuna, Region, Contact
# Register your models here.

admin.site.register(Perfil)
admin.site.register(Inmueble)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Contact)
