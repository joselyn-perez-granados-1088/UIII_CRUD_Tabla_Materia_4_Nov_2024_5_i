from django.shortcuts import render,redirect
from .models import Materia

# Create your views here.

def inicio_vista(request):
    lasmaterias=Materia.objects.all()
    return render(request,'gestionarMateria.html',{"mismaterias":lasmaterias})

def registrartMaterias(request):
    codido=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credito=request.POST["numcreditos"]

    guardarmateria=Materia.objects.create(codido=codido,nombre=nombre,credito=credito) 

    return redirect('/')

def seleccionarMateria(request,codido):
    materia=Materia.objects.get(codido=codido)
    return render(request,"editarMateria.html",{"mismaterias":materia})

def editarMateria(request):
    codido=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credito=request.POST["numcreditos"]

    materia=Materia.objects.get(codido=codido)

    materia.nombre=nombre
    materia.credito=credito
    materia.save()

    return redirect('/')

def borrarMateria(request,codido):
    materia=Materia.objects.get(codido=codido)
    materia.delete()

    return redirect("/")