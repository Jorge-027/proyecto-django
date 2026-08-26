from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path("v1/", views.vista1, name="app2-v1"),
    path("v2/", views.vista2, name="app2-v2"),
]
def vista1(request):
    return HttpResponse("<h1>App2 - Vista1</h1><p>Hola desde App2/Vista1</p>")

def vista2(request):
    return HttpResponse("<h1>App2 - Vista2</h1><p>Hola desde App2/Vista2</p>")
# Create your views here.
