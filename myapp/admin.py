from django.contrib import admin
from .models import Project, Task

# Register your models here.
admin.site.register(Project)  # registramos nuestro modelo al django admin
admin.site.register(Task)
