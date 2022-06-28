from django import forms
from .models import *


class FormularioInicial(forms.Form):
    nombre1_form = forms.CharField(label="Tu Nombre: ", max_length=40)
    apellido1_form = forms.CharField(label="Tu Apellido: ", max_length=40)
    email1_form = forms.EmailField(label="Tu Email: ", max_length=40)
    celular1_form = forms.IntegerField(
        label="Tu Celular: ",
    )


class FormularioIntermedio(forms.Form):
    nombre2_form = forms.CharField(label="Tu Nombre: ", max_length=40)
    apellido2_form = forms.CharField(label="Tu Apellido: ", max_length=40)
    email2_form = forms.EmailField(label="Tu Email: ", max_length=40)
    celular2_form = forms.IntegerField(
        label="Tu Celular: ",
    )


class FormularioAvanzado(forms.Form):
    nombre3_form = forms.CharField(label="Tu Nombre: ", max_length=40)
    apellido3_form = forms.CharField(label="Tu Apellido: ", max_length=40)
    email3_form = forms.EmailField(label="Tu Email: ", max_length=40)
    celular3_form = forms.IntegerField(
        label="Tu Celular: ",
    )
