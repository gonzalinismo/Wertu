from django.db import models
from suscripciones.models import Suscripcion

# Create your models here.
class TipoPago(models.Model):
	idTipoPago= models.IntegerField(primary_key=True, null=False, blank=False)
	nombreTipoPago= models.CharField(max_length=20)
	def __str__(self):
		return str(self.nombreTipoPago)

class Pago(models.Model):
	idPago= models.AutoField(primary_key=True)
	montoPago= models.DecimalField(decimal_places=2, max_digits=5)
	fechaPago= models.DateField()
	tipoPagoRegistrado= models.ForeignKey(TipoPago, on_delete=models.CASCADE)
	suscripcionPagada= models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.idPago)