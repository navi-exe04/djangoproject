from django.http import HttpResponse

# Create your views here.


def hello(request):  # resquest nos permite obtener datos del usuario
    # Regresamos una respuesta http para el mensaje de hola mundo
    return HttpResponse("<h1>Hello World</h1>")


def about(request):
    return HttpResponse("<h2>About</h2>")
