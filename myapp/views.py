from django.http import HttpResponse, JsonResponse
# podemos importar las tablas de la db para manipularlas
from .models import Project, Task
# esta funcion permite obtener un objeto o mandar un error 404 directamente
from django.shortcuts import get_object_or_404, render

# Create your views here.


# resquest nos permite obtener datos del usuario, tambien podemos especificar los datos a esperar
def index(request):
    title = "Django Course!!!"
    # renderizamos la vista que necesitamos
    return render(request, 'index.html', {
        # podemos pasar parametros con un diccionario
        "title": title
    })


def about(request):
    username = 'Raul Langle'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    # Regresamos una respuesta http para el mensaje de hola
    return HttpResponse(f"<h1>Hello {username}</h1>")


def projects(request):
    # trae todos los elementos de la tabla Project
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    # Devuelve un objeto JSON para el navegador
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
