from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.nombre

class Diagnostico(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Diagnóstico de {self.proyecto.nombre} - {self.fecha}"
