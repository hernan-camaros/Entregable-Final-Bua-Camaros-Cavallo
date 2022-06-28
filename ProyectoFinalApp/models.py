from django.db import models


class ClaseInicial(models.Model):
    nombre1_clase = models.CharField(max_length=40)
    apellido1_clase = models.CharField(max_length=40)
    email1_clase = models.EmailField(max_length=40)
    celular1_clase = models.IntegerField()


class ClaseIntermedia(models.Model):
    nombre2_clase = models.CharField(max_length=40)
    apellido2_clase = models.CharField(max_length=40)
    email2_clase = models.EmailField(max_length=40)
    celular2_clase = models.IntegerField()


class ClaseAvanzada(models.Model):
    nombre3_clase = models.CharField(max_length=40)
    apellido3_clase = models.CharField(max_length=40)
    email3_clase = models.EmailField(max_length=40)
    celular3_clase = models.IntegerField()
