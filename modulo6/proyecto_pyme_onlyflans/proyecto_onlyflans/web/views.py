from django.shortcuts import render
from .models import Flan
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
