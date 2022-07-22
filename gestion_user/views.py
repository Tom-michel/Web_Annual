from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Membre
from .forms import UserForm, MembreForm, UserUpadateForm

from projets.models import Tache
from projets.forms import CreateTaskForm

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

    user_form = UserUpadateForm(instance=use)
    member_form = MembreForm(instance=use.membre)
    err1 = ""
    err2 = ""

    if request.method == 'POST':
        user_form = UserUpadateForm(data=request.POST, instance=use)
        member_form = MembreForm(request.POST, request.FILES, instance=use.membre)
        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            user.save()
            membre = member_form.save(commit=False)
            membre.user = user
            membre.save()
            return HttpResponseRedirect('../profil_membre/'+id_u)
        else:
            err1 = user_form.errors
            err2 = member_form.errors
            context = {
                'err1':err1, 'err2':err2,
                'user_form':user_form, 'member_form':member_form
            }
            return render(request, 'gestion_user/inscription.html', context)
    else:

        # trouver les taches confiées au membre
        membre = Membre.objects.get(id=use.membre.id)
        task_list = []
        task_list1 = []
        task_list2 = []
        task_list3 = []
        for task in Tache.objects.all():
            if membre in task.membres.all():
                task_list.append(task)
                if task.etat == 'etat 1':
                    task_list1.append(task)
                if task.etat == 'etat 2':
                    task_list2.append(task)
                if task.etat == 'etat 3':
                    task_list3.append(task)
        nbre = len(task_list)
        nbre1 = len(task_list1)
        nbre2 = len(task_list2)
        nbre3 = len(task_list3)
        # task_list1 = Tache.objects.filter(etat='etat 1')
        # task_list2 = Tache.objects.filter(etat='etat 2')
        # task_list3 = Tache.objects.filter(etat='etat 3')
        create_form = CreateTaskForm()
        err_task = ""

        context = {
            'use':use,
            'err1':err1, 'err2':err2,
            'user_form':user_form, 'member_form':member_form,

            # taches du membre
            'task_list':task_list,
            'task_list1':task_list1,
            'task_list2':task_list2,
            'task_list3':task_list3,
            'create_form':create_form,
            'err_task':err_task,
            'nbre':nbre, 'nbre1':nbre1, 'nbre2':nbre2, 'nbre3':nbre3,
        }
        return render(request, 'gestion_user/profil_membre.html', context)



# supprimer un compte

def supprimer_compte(request, id_u):
    user = User.objects.get(id=id_u)
    user.delete()
    return HttpResponseRedirect('/')

def supprimer_compte_2(request, id_u):
    user = User.objects.get(id=id_u)
    user.delete()
    return HttpResponseRedirect('../member_list')



# se déconnecter

@login_required(login_url='connexion')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



# consulter la liste des membres

def member_list(request):
    member_list = Membre.objects.all
    context = {
        'member_list':member_list,
    }
    return render(request, 'gestion_user/member_list.html', context)