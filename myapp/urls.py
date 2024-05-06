from django.urls import path
from . import views

# lo ideal es que cada aplicación tenga su propias urls
# aqui podemos decidir las urls de nuestra aplicacion
urlpatterns = [
    path('', views.hello),
    path('about/', views.about)
]
