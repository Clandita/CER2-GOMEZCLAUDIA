from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import correspondencia

# Create your views here.

def home(request):

    return render(request,'core/home.html')


def lista(request):
    busqueda=request.GET.get('buscar')
    cor_lista=correspondencia.objects.all()

    if busqueda:
        cor_lista= correspondencia.objects.filter(Q(nro_residencia__numero=busqueda)).distinct()

    return render(request, "core/lista.html",{"lista":cor_lista})
    