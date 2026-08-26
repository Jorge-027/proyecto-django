from django.http import HttpResponse

def vista1(request):
    return HttpResponse("<h1>App1 - Vista1</h1><p>Hola desde App1/Vista1</p>")

def vista2(request):
    return HttpResponse("<h1>App1 - Vista2</h1><p>Hola desde App1/Vista2</p>")