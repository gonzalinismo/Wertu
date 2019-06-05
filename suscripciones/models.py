from django.db import models
from tiendas.models import Tienda
from django.forms import ModelForm
# Create your models here.
class TipoSuscripcion(models.Model):
	idTipoSuscripcion= models.IntegerField(primary_key=True, null=False, blank=False)
	descripcionTipoSuscripcion= models.CharField(max_length=200)
	precioTipoSuscripcion= models.DecimalField(decimal_places=2, max_digits=5)
	duracionTipoSuscripcion= models.IntegerField()
	def __str__(self):
		return str(self.descripcionTipoSuscripcion)

class Suscripcion(models.Model):
	tiendaSuscripta= models.ForeignKey(Tienda, on_delete=models.CASCADE)
	fechaInicio= models.DateField(auto_now_add=True)
	fechaCancelacion= models.DateField(auto_now_add=False)				
	suscripcionElegida= models.ForeignKey(TipoSuscripcion, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.tiendaSuscripta)

class SuscripcionForm(ModelForm):
	class Meta:
		model= Suscripcion
		fields=['tiendaSuscripta', 'suscripcionElegida']


