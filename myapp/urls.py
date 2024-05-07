from django.urls import path
from . import views

# lo ideal es que cada aplicación tenga su propias urls
# aqui podemos decidir las urls de nuestra aplicacion
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    # podemos especificar que parametros esperamos dentro de la url
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks)
]
