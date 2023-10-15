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
    return render(request, "appweb/Libros.html")

# enlace de inicio
def libraries(request):
    return render(request, "appweb/Bibliotecas.html")

# enlace de inicio
def about(request):
    return render(request, "appweb/Acerca.html")

# enlace de inicio
def login(request):
    #return HttpResponse("Login")
    return render(request, "appweb/Login.html")