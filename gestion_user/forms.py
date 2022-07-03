from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Membre


# formulaire pour créer un user
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            'username',
            'last_name',
            'password1',
            'password2'
        ]

# formulaire pour modifier un user
class UserUpadateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = [
            'username',
            'last_name',
        ]

# formulaire pour créer un membre
class MembreForm(forms.ModelForm):
    class Meta():
        model = Membre
        fields = [
            'photo',
            'ville',
            'quartier',
            'telephone',
            'fonction',
            'description'
        ]
