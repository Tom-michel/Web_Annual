from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tache

# formulaire pour créer une tâche
class CreateTaskForm(forms.ModelForm):
    class Meta():
        model = Tache
        fields = [
            'intitule',
            'progression',
        ]