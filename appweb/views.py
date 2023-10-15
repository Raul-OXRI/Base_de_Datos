from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

# enlace de inicio
def home(request):
    #se va a cambiar para que redirecciones al template de inicio la que creamos con html y css
    #return HttpResponse("Home")
    return render(request, "appweb/Home.html")

# enlace de inicio
def books(request):
    return HttpResponse("Libros")

# enlace de inicio
def libraries(request):
    return HttpResponse("Bibliotecas")

# enlace de inicio
def about(request):
    return HttpResponse("Acerca")

# enlace de inicio
def login(request):
    return HttpResponse("Login")