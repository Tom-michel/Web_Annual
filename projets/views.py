from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from gestion_user.views import connexion

# Create your views here.


# page d'accueil

# @login_required(login_url='index')
def accueil(request):
    if request.user.is_authenticated:
            return render(request, 'projets/accueil.html')
    else:
        return render(request, 'gestion_user/index.html')


# liste des tâches

def task_list(request):
    context = {

    }
    return render(request, 'projets/task_list.html')

