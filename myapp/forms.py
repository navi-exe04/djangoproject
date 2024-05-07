from django import forms


# podemos definir la estructura de los form que vayamos a utilizar
class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de la tarea", max_length=200)
    description = forms.CharField(
        label="Descripcion de la tarea", widget=forms.Textarea)
