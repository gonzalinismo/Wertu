from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):	
	return render(request,"index.html",{})

@login_required
def inicio(request):
    return render(request,"inicio.html",{})

@login_required
def miPerfil(request):	
    return render(request,"miPerfil.html",{})

@login_required
def misPagos(request):
    return render(request,"misPagos.html",{})