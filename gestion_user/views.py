from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Membre

# Create your views here.


# page d'accueil

def index(request):
    return render(request, 'gestion_user/index.html')


 # se connecter à son compte
def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('email-login')
        password = request.POST.get('password-login')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_authenticated:
                logout(request)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            msg = messages.info(request, "votre Adresse mail ou votre Mot de passe est incorrect, veuillez réessayer !")
            context = {
                'msg':msg
            }
            return render(request, 'gestion_user/connexion.html', context)
    else :
        return render(request, 'gestion_user/connexion.html')




# se déconnecter
@login_required(login_url='connexion')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
