from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tache, Projet

# formulaire pour créer une tâche
class CreateTaskForm(forms.ModelForm):
    class Meta():
        model = Tache
        fields = [
            'intitule',
            'progression',
        ]


# formulaire pour créer un projet
class CreateProjectForm(forms.ModelForm):
    class Meta():
        model = Projet
        fields = [
            'titre',
            'description'
        ]


# formulaire pour modifier un projet
class EditProjectForm(forms.ModelForm):
    class Meta():
        model = Projet
        fields = [
            'titre',
            'description',
            'visibilite'
        ]
