from django.shortcuts import render
from django.urls import path
from . import views
from django.http import HttpResponse

def vista1(request):
    return HttpResponse("<h1>App1 - Vista1</h1><p>Hola desde App1/Vista1</p>")

def vista2(request):
    return HttpResponse("<h1>App1 - Vista2</h1><p>Hola desde App1/Vista2</p>")

urlpatterns = [
    path("v1/", views.vista1, name="app1-v1"),
    path("v2/", views.vista2, name="app1-v2"),
]
# Create your views here.
