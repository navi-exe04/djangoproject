from django.urls import path
from . import views

# lo ideal es que cada aplicación tenga su propias urls
# aqui podemos decidir las urls de nuestra aplicacion
urlpatterns = [
    # podemos definir nombres para las urls para no definirlas
    # en toda la aplicación, y solo invocar su nombre
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    # podemos especificar que parametros esperamos dentro de la url
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('project_detail/<int:id>', views.project_details, name="project"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project")
]
