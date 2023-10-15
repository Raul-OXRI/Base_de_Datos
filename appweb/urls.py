from django.urls import path
from appweb import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('Libros', views.books, name="Libros"),
    path('Bibliotecas', views.libraries, name="Bibliotecas"),
    path('Acerca', views.about, name="Acerca"),
    path('Login', views.login, name="Login"),
]