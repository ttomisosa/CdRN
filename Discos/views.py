from django.shortcuts import render
from .models import disco

def Discos1(request):
    discos = disco.objects.all()
    return render(request, 'discos/Discos.html', {'discos': discos})
