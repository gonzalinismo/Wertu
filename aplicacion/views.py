from django.shortcuts import render
from tiendas.models import Tienda, Categoria
# Create your views here.
def app(request):
	categorias= Categoria.objects.all()
	print(categorias)
	tiendas= Tienda.objects.filter(categoriaTienda=1)
	categoriaElegida= Categoria.objects.get(idCategoriaTienda=1)	
	context={'categorias':categorias, 'tiendas':tiendas, 'categoriaElegida':categoriaElegida}
	return render(request, 'aplicacion.html', context)
	
def filtrarTiendas(request, categoria):
	categorias= Categoria.objects.all()
	categoriaElegida= Categoria.objects.get(idCategoriaTienda=categoria)	
	tiendas= Tienda.objects.filter(categoriaTienda=categoria)
	context={'categorias':categorias, 'tiendas':tiendas, 'categoriaElegida':categoriaElegida}
	return render(request, 'aplicacion.html', context)	