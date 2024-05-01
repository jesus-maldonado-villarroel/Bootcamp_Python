from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Flan, ContactForm
from .form import ContactFormForm
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
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('exito')

    else:
        form = ContactFormForm()

    return render(request, 'contactus.html', {'form': form})


def exito(request):
    return render(request, 'exito.html', {})
