from django.urls import path

from . import views
from tiendas.views import misTiendas, agregarTienda, eliminarTienda, editarTienda
from aplicacion.views import app, filtrarTiendas
urlpatterns = [
    path('', views.index, name='index'),
    path('inicio', views.inicio, name='inicio'),
    path('misTiendas', misTiendas, name='misTiendas'),
    path('editarTienda/<int:cuit>', editarTienda, name='editarTienda'),
    path('agregarTienda', agregarTienda, name='agregarTienda'),
    path('eliminarTienda/<int:cuit>', eliminarTienda, name='eliminarTienda'),
    path('miPerfil', views.miPerfil, name='miPerfil'),
    path('misPagos', views.misPagos, name='misPagos'),
    path('app', app, name='app'),
    path('filtrarTiendas/<int:categoria>', filtrarTiendas, name='filtrarTiendas'),



    ]