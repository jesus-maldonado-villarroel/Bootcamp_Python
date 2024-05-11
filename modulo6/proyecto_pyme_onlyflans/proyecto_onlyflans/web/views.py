from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Flan, ContactForm, Flon
from .form import ContactFormModelForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {'flanes': flanes_publicos}
    return render(request, 'index.html', context)


def acerca(request):
    return render(request, 'about.html', {})


def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {'flanes': flanes_privados}
    return render(request, 'welcome.html', context)


def base(request):
    return render(request, 'base.html', {})


def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')

    else:
        form = ContactFormModelForm()

    return render(request, 'contactus.html', {'form': form})


def exito(request):
    return render(request, 'exito.html', {})


def login(request):
    return render(request, 'login.html', {})


def logout(request):
    return render(request, 'logout.html', {})


def promocion(request):
    flones_publicos = Flon.objects.filter(is_private=False)
    context = {'flones': flones_publicos}
    return render(request, 'promocion.html', context)
