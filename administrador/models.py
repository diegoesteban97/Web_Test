from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

class User(models.Model):
    usuario = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=12)
    correo = models.CharField(max_length=30)
    telefono = models.IntegerField()
    fechaRegistro = models.DateTimeField(auto_now_add=True)