from django.http import HttpResponse, JsonResponse
# podemos importar las tablas de la db para manipularlas
from .models import Project, Task
# esta funcion permite obtener un objeto o mandar un error 404 directamente
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

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


def create_task(request):
    if request.method == 'GET':
        # renderiza la vista del formulario
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        # podemos procesar informacion recibida desde front
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=2
        )
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
    else:
        # podemos procesar informacion recibida desde front
        Project.objects.create(
            name=request.POST['name'],
        )
        return redirect('projects')


def project_details(request, id):
    # obtenemos el proyecto en especifico
    project = get_object_or_404(Project, id=id)
    # obtenemos las tasks del proyecto
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'project_details.html', {
        'project': project,
        'tasks': tasks
    })
