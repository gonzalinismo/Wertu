from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Provincia(models.Model):
	idProvincia= models.IntegerField(null=False, primary_key=True, unique=True)
	nombreProvincia= models.CharField(max_length=40)
	def __str__(self):
		return str(self.nombreProvincia)

class Ciudad(models.Model):
	codigoPostal= models.IntegerField(primary_key=True, null=False, unique=True)
	nombreCiudad= models.CharField(max_length=40)
	provincia= models.ForeignKey(Provincia, null=False, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.codigoPostal)

class Categoria(models.Model):
	idCategoriaTienda= models.IntegerField(primary_key=True, null=False, unique=True)
	nombreCategoriaTienda= models.CharField(max_length=30)
	def __str__(self):
		return str(self.nombreCategoriaTienda)

class Tienda(models.Model):
	titular= models.ForeignKey(User, on_delete=models.CASCADE)
	nombreTienda= models.CharField(max_length=100, blank= False, default="test")
	cuit= models.IntegerField(primary_key=True, unique=True, null=False, blank=False)
	ciudad= models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.CASCADE)	
	direccion= models.CharField(max_length=100)
	categoriaTienda= models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
	telefono= models.CharField(max_length=20)
	bio= models.CharField(max_length=200, null=True, blank=True)
	face= models.URLField(null=True, blank=True)
	insta= models.URLField(null=True, blank=True)
	mail= models.CharField(max_length=200, null=True, blank=True)
	web= models.URLField(null=True, blank=True)
	imagenPrincipal= models.ImageField(null=True, blank=True)
	imagenAdicional1= models.ImageField(null=True, blank=True)
	imagenAdicional2= models.ImageField(null=True, blank=True)
	imagenAdicional3= models.ImageField(null=True, blank=True)
		
	def __str__(self):
		return str(self.cuit)

