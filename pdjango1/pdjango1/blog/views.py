from django.shortcuts import render
from blog.models import Entrada
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     # return HttpResponse("Bienvenido al blog")
#     verentradas = Entrada.objects.all().order_by('-fecha')[:5]
#     output = ', '.join([p.titulo for p in verentradas])
#     return HttpResponse(output)

def index(request):
    entradas = Entrada.objects.all()
    entrada_string = "Entradas <br/>"
    entrada_string += '<br/> '.join(["id: %s, titulo: %s"% (e.id, e.titulo) for e in entradas])
    return HttpResponse(entrada_string)