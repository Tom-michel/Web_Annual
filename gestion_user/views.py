from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Membre
from .forms import UserForm, MembreForm, UserUpadateForm

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


# s'incrire

def inscription(request):
    user_form = UserForm()
    member_form = MembreForm()
    err1 = ""
    err2 = ""

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        member_form = MembreForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            user.save()
            membre = member_form.save(commit=False)
            membre.user = user
            membre.save()

            # connecter le user
            user_log = authenticate(username=username, password=password)
            if user_log:
                if user.is_authenticated:
                    logout(request)
                login(request, user_log)
            # le renvoyer vers la page d'accueil 2
            return HttpResponseRedirect('/')
        else:
            err1 = user_form.errors
            err2 = member_form.errors
            context = {
                'err1':err1, 'err2':err2,
                'user_form':user_form, 'member_form':member_form
            }
            return render(request, 'gestion_user/inscription.html', context)
    else:
        context = {'user_form':user_form, 'member_form':member_form}
        return render(request, 'gestion_user/inscription.html', context)



# consulter le profil d'un membre
@login_required(login_url='connexion')
def profil_membre(request, id_u):
    use = User.objects.get(id=id_u)
    context = {
        'use':use,
    }
    return render(request, 'gestion_user/profil_membre.html', context)



# supprimer un compte

def supprimer_compte(request, id_u):
    user = User.objects.get(id=id_u)
    user.delete()
    return HttpResponseRedirect('/')



# se déconnecter

@login_required(login_url='connexion')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
