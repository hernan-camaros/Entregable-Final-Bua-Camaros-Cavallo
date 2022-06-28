from django.shortcuts import render
from ProyectoFinalApp.models import *
from ProyectoFinalApp.forms import *


def inicio(request):
    return render(
        request,
        r"C:\Users\Santiago\Desktop\Python\Entregable-Final-Bua-Camaros-Cavallo\ProyectoFinal\ProyectoFinalApp\templates\index.html",
    )


def inscripcion(request):

    return render(request, "inscripcion.html", {})


def agregar_inicial(request):

    if request.method == "POST":

        curso1 = FormularioInicial(request.POST)

        if FormularioInicial.is_valid():

            informacion = curso1.cleaned_data

            curso1 = ClaseInicial(
                nombre=informacion["nombre_1"],
                apellido=informacion["apellido_1"],
                emails=informacion["email_1"],
                celular=informacion["celular_1"],
            )

            curso1.save()

            return render(request, "index.html")

    else:
        curso1 = FormularioInicial()

    return render(request, "formulario_inicial.html", {"form": FormularioInicial})


def agregar_intermedio(request):

    if request.method == "POST":

        curso2 = FormularioIntermedio(request.POST)

        if curso2.is_valid():

            informacion = curso2.cleaned_data

            curso2 = ClaseIntermedia(
                nombre=informacion["nombre_2"],
                apellido=informacion["apellido_2"],
                emails=informacion["email_2"],
                celular=informacion["celular_2"],
            )

            curso2.save()

            return render(request, "index.html")

    else:
        curso2 = FormularioIntermedio()

    return render(request, "formulario_intermedio.html", {"form": curso2})


def agregar_avanzado(request):

    if request.method == "POST":

        curso3 = FormularioAvanzado(request.POST)

        if curso3.is_valid():

            informacion = curso3.cleaned_data

            curso3 = ClaseAvanzada(
                nombre=informacion["nombre_3"],
                apellido=informacion["apellido_3"],
                emails=informacion["email_3"],
                celular=informacion["celular_3"],
            )

            curso3.save()

            return render(request, "index.html")

    else:
        curso3 = FormularioAvanzado()

    return render(request, "formulario_avanzado.html", {"form": curso3})
