from django.contrib import admin
from .models import User, Usuario, Inmueble, Comuna, Region
# Register your models here.

admin.site.register(User)
admin.site.register(Usuario)
admin.site.register(Inmueble)
admin.site.register(Comuna)
admin.site.register(Region)
