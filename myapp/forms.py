from django import forms


# podemos definir la estructura de los form que vayamos a utilizar
class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de la tarea", max_length=200, widget=forms.Textarea(
        attrs={'class': ''}))  # podemos agregar clases a los inputs de los forms
    description = forms.CharField(
        label="Descripcion de la tarea", widget=forms.Textarea)


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)
