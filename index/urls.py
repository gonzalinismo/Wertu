from django.urls import path

from . import views
from tiendas.views import misTiendas, agregarTienda, eliminarTienda, editarTienda

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio', views.inicio, name='inicio'),
    path('misTiendas', misTiendas, name='misTiendas'),
    path('editarTienda/<int:cuit>', editarTienda, name='editarTienda'),
    path('agregarTienda', agregarTienda, name='agregarTienda'),
    path('eliminarTienda/<int:cuit>', eliminarTienda, name='eliminarTienda'),
    path('miPerfil', views.miPerfil, name='miPerfil'),
    path('misPagos', views.misPagos, name='misPagos'),

    ]