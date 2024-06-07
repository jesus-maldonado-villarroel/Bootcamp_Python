from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil, Inmueble, Contact


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de usuario',
            'email': 'Correo electronico',
            'password1': 'Contraseña',
            'password2': 'Repita la contraseña'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),
        }


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('rut', 'direccion', 'telefono', 'tipo_usuario')
        labels = {
            'rut': 'RUT',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'tipo_usuario': 'Tipo de Usuario'
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su RUT'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su teléfono'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-select', 'id': 'id_tipo_usuario'}),
        }


class InmuebleForm(forms.ModelForm):

    class Meta:
        model = Inmueble
        fields = ('nombre', 'descripcion', 'm2_contruidos', 'm2_totales', 'cantidad_estacionamientos', 'cantidad_habitaciones',
                  'cantidad_baños', 'direccion', 'id_comuna', 'id_region', 'tipo_inmueble', 'precio_mensual', 'estado')

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'm2_contruidos': 'Metros cuadrados construidos',
            'm2_totales': 'Metros cuadrados totales',
            'cantidad_estacionamientos': 'N° estacionamientos',
            'cantidad_habitaciones': 'N° habitaciones',
            'cantidad_baños': 'N° baños',
            'direccion': 'Dirección',
            'id_comuna': 'Comuna',
            'id_region': 'Región',
            'tipo_inmueble': 'Tipo de Inmueble',
            'precio_mensual': 'Precio mensual',
            'estado': 'Disponible'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'm2_contruidos': forms.NumberInput(attrs={'class': 'form-control'}),
            'm2_totales': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_estacionamientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_baños': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_comuna': forms.Select(attrs={'class': 'form-select', 'id': 'id_comuna'}),
            'id_region': forms.Select(attrs={'class': 'form-select', 'id': 'id_region'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-select', 'id': 'id_tipo_inmueble'}),
            'precio_mensual': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('correo', 'celular', 'name', 'mensaje')
        labels = {
            'correo': 'Correo',
            'celular': 'Celular',
            'name': 'Nombre',
            'mensaje': 'Mensaje'
        }
