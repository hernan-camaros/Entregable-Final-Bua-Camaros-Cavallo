from django.shortcuts import render
from ProyectoFinalApp.models import *
from ProyectoFinalApp.forms import *


def inicio(request):
    return render(
        request,
        "index.html",
    )


def inscripcion(request):

    return render(request, "inscripcion.html", {})


def agregar_inicial(request):

    if request.method == "POST":

        curso1 = FormularioInicial(request.POST)

        if curso1.is_valid():

            informacion = curso1.cleaned_data

            curso1 = ClaseInicial(
                nombre1_clase=informacion["nombre1_form"],
                apellido1_clase=informacion["apellido1_form"],
                email1_clase=informacion["email1_form"],
                celular1_clase=informacion["celular1_form"],
            )

            curso1.save()

            return render(request, "index.html")

    else:
        curso1 = FormularioInicial()

    return render(request, "formulario_inicial.html", {"form": curso1})


def agregar_intermedio(request):

    if request.method == "POST":

        curso2 = FormularioIntermedio(request.POST)

        if curso2.is_valid():

            informacion = curso2.cleaned_data

            curso2 = ClaseIntermedia(
                nombre2_clase=informacion["nombre2_form"],
                apellido2_clase=informacion["apellido2_form"],
                email2_clase=informacion["email2_form"],
                celular2_clase=informacion["celular2_form"],
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
                nombre3_clase=informacion["nombre3_form"],
                apellido3_clase=informacion["apellido3_form"],
                email3_clase=informacion["email3_form"],
                celular3_clase=informacion["celular3_form"],
            )

            curso3.save()

            return render(request, "index.html")

    else:
        curso3 = FormularioAvanzado()

    return render(request, "formulario_avanzado.html", {"form": curso3})
