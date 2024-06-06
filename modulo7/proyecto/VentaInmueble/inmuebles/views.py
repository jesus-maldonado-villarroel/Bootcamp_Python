from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Inmueble, Perfil, Region, Comuna, Contact
from .forms import UserForm, PerfilForm, InmuebleForm, ContactForm
from django.contrib.auth import login, authenticate
# Create your views here.


def index(request):

    return render(request, 'index.html', {})


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            ultimo_usuario_creado = authenticate(
                request, username=username, password=password)
            login(request, ultimo_usuario_creado)
            return HttpResponseRedirect('/profile/')
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    else:
        form = UserForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)


@login_required(login_url='/login/')
def profile(request):
    usuario = request.user
    perfil = Perfil.objects.filter(usuario=usuario).first()
    tipo = None
    if perfil:
        tipo = perfil.tipo_usuario

    context = {'perfil': perfil, 'tipo': tipo}
    return render(request, 'profile.html', context)


@login_required(login_url='/login/')
def register_profile(request):
    usuario = request.user
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            usuario = usuario
            tipo = form.cleaned_data['tipo_usuario']
            rut = form.cleaned_data['rut']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            email = usuario.email

            datos = Perfil(
                usuario=usuario,
                tipo_usuario=tipo,
                rut=rut,
                direccion=direccion,
                telefono=telefono,
                email=email,
            )
            datos.save()
            return HttpResponseRedirect('/profile/')

    else:
        form = PerfilForm()
        context = {
            'form': form,
            'title': 'Crear perfil'
        }
    return render(request, 'register_profile.html', context)


@login_required(login_url='/login/')
def update_profile(request):
    usuario = request.user
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = Perfil.objects.filter(
                usuario=usuario).update(**form.cleaned_data)
            return HttpResponseRedirect('/profile/')

    else:

        perfil = Perfil.objects.filter(usuario=usuario)
        if perfil.exists():
            perfil = perfil.first()
            form = PerfilForm(instance=perfil)
            context = {
                'form': form,
                'title': 'Actualizar Perfil'
            }
            return render(request, 'register_profile.html', context)


@login_required(login_url='/login/')
def register_inmueble(request, username):
    # usuario = User.objects.get(username=username)
    usuario = request.user
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario
    if request.method == "POST":
        form = InmuebleForm(request.POST)
        if form.is_valid():
            usuario = usuario
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            m2_contruidos = form.cleaned_data['m2_contruidos']
            m2_totales = form.cleaned_data['m2_totales']
            cantidad_estacionamientos = form.cleaned_data['cantidad_estacionamientos']
            cantidad_habitaciones = form.cleaned_data['cantidad_habitaciones']
            cantidad_baños = form.cleaned_data['cantidad_baños']
            direccion = form.cleaned_data['direccion']
            comuna = form.cleaned_data['id_comuna']
            region = form.cleaned_data['id_region']
            tipo_inmueble = form.cleaned_data['tipo_inmueble']
            precio_mensual = form.cleaned_data['precio_mensual']
            estado = form.cleaned_data['estado']

            datos = Inmueble(
                id_usuario=usuario,
                nombre=nombre,
                descripcion=descripcion,
                m2_contruidos=m2_contruidos,
                m2_totales=m2_totales,
                cantidad_estacionamientos=cantidad_estacionamientos,
                cantidad_habitaciones=cantidad_habitaciones,
                cantidad_baños=cantidad_baños,
                direccion=direccion,
                id_comuna=comuna,
                id_region=region,
                tipo_inmueble=tipo_inmueble,
                precio_mensual=precio_mensual,
                estado=estado
            )
            datos.save()
            return HttpResponseRedirect('/inmuebles/')
    else:
        form = InmuebleForm()
        context = {
            'form': form,
            'tipo': tipo,
            'title': 'Registrar Inmueble'
        }
        return render(request, 'register_inmueble.html', context)


@login_required(login_url='/login/')
def obtener_inmueble(request):
    usuario = request.user
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario
    inmuebles = Inmueble.objects.filter(id_usuario=usuario)
    context = {
        'inmuebles': inmuebles,
        'tipo': tipo,
        'title': 'Inmuebles Registrados'
    }
    return render(request, 'inmuebles.html', context)


@login_required(login_url='/login/')
def update_inmueble(request, inmueble_id):
    usuario = request.user
    inmueble = Inmueble.objects.filter(
        id=inmueble_id, id_usuario=usuario).first()
    if not inmueble:
        return HttpResponseRedirect('/inmuebles/')

    if request.method == "POST":
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inmuebles/')
    else:
        form = InmuebleForm(instance=inmueble)

    context = {
        'form': form,
        'title': 'Actualizar Inmueble'
    }
    return render(request, 'register_inmueble.html', context)


@login_required(login_url='/login/')
def listar_inmuebles_disponibles(request):

    comuna = request.GET.get('comuna')
    region = request.GET.get('region')
    keyword = request.GET.get('keyword')
    tipo_inmueble = request.GET.get('tipo_inmueble')

    viviendas = Inmueble.objects.filter(estado=True)

    if comuna:
        viviendas = viviendas.filter(
            id_comuna__nombre_comuna__icontains=comuna)

    if region:
        viviendas = viviendas.filter(
            id_region__nombre_region__icontains=region)

    if keyword:
        viviendas = viviendas.filter(descripcion__icontains=keyword)

    if tipo_inmueble:
        viviendas = viviendas.filter(tipo_inmueble=tipo_inmueble)

    regiones = Region.objects.all()
    comunas = Comuna.objects.all()

    context = {
        'viviendas': viviendas,
        'regiones': regiones,
        'comunas': comunas,
        'title': 'Viviendas Disponibles'
    }
    return render(request, 'listar_inmuebles.html', context)


@login_required(login_url='/login/')
def contact(request, id):
    usuario = request.user
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario
    inmueble = Inmueble.objects.get(pk=id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            celular = form.cleaned_data['celular']
            name = form.cleaned_data['name']
            mensaje = form.cleaned_data['mensaje']
            nombre_inmueble = inmueble.nombre
            arrendador = inmueble.id_usuario

            data = Contact(
                nombre_inmueble=nombre_inmueble,
                correo=correo,
                celular=celular,
                arrendador=arrendador,
                name=name,
                mensaje=mensaje,
            )
            data.save()
            return HttpResponseRedirect('/inmuebles_disponibles/')

    form = ContactForm()
    context = {
        'form': form,
        'title': 'Contacta al Propietario',
        'tipo': tipo
    }
    return render(request, 'register_inmueble.html', context)


@login_required(login_url='/login/')
def messages(request):
    usuario = request.user
    messages = Contact.objects.filter(arrendador=usuario)
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario

    context = {
        'messages': messages,
        'tipo': tipo
    }
    return render(request, 'contact.html', context)
