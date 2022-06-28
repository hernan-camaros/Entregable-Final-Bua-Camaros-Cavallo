from django.contrib import admin
from django.urls import path
from ProyectoFinalApp import views
from ProyectoFinalApp.views import *


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("agregarinicial/", views.agregar_inicial, name="inicial"),
    path("agregarintermedio/", views.agregar_intermedio, name="intermedio"),
    path("agregaravanzado/", views.agregar_avanzado, name="avanzado"),
    path("inscribite/", views.inscripcion, name="inscripcion"),
]
