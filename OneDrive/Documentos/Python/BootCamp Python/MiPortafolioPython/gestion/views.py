from django.shortcuts import render, redirect
from .models import Proyecto
from .forms import ProyectoForm

def home(request):
    return render(request, "gestion/home.html")

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "gestion/lista_proyectos.html", {"proyectos": proyectos})

def nuevo_proyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, "gestion/nuevos_proyectos.html", {"form": form})
