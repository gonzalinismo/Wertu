from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import Tienda
from .forms import TiendaForm
# Create your views here.
@login_required
def misTiendas(request):
	tiendas= Tienda.objects.filter(titular=request.user)
	context={'tiendas':tiendas}
	return render(request,"misTiendas.html",context)

@login_required
def agregarTienda(request):
	registered = False
	if request.method == 'POST':
		tienda_form = TiendaForm(data=request.POST) 		
		print(tienda_form)       
		if tienda_form.is_valid():
			tienda = tienda_form.save(commit=False)
			tienda.titular=request.user
			tienda.save()                    
			registered = True
			return HttpResponseRedirect('../../misTiendas')
		else:
			print(tienda_form.errors)
	else:
		tienda_form = TiendaForm()		
	return render(request,'agregarTienda.html',
	{'tienda_form':tienda_form,                           
	'registered':registered})

@login_required
def eliminarTienda(request, cuit):	
	tienda= Tienda.objects.filter(cuit=cuit)
	tienda.delete()
	return HttpResponseRedirect('../../misTiendas')

@login_required
def editarTienda(request, cuit):	
	tienda= Tienda.objects.filter(cuit=cuit)
	tienda.delete()
	return HttpResponseRedirect('../../misTiendas')	