from django.contrib import admin
from .models import Inmueble, User, Region, Comuna

# Register your models here.

admin.site.register(Inmueble)
admin.site.register(User)
admin.site.register(Region)
admin.site.register(Comuna)
