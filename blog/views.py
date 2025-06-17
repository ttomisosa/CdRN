from django.shortcuts import render
from .models import Publicacion

def lista_public(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'blog/lista_public.html', {'publicaciones': publicaciones})
