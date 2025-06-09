from django.shortcuts import render

def lista_public(request):
    return render(request, 'blog/lista_public.html', {})