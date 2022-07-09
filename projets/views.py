from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Tache
from .forms import CreateTaskForm
from gestion_user.views import connexion

# Create your views here.


# page d'accueil

# @login_required(login_url='index')
def accueil(request):
    if request.user.is_authenticated:
            return render(request, 'projets/accueil.html')
    else:
        return render(request, 'gestion_user/index.html')



# créer une tache, lister les tâches

def task_list(request):
    task_list = Tache.objects.all()
    task_list1 = Tache.objects.filter(etat='etat 1')
    task_list2 = Tache.objects.filter(etat='etat 2')
    task_list3 = Tache.objects.filter(etat='etat 3')
    create_form = CreateTaskForm()
    err_task = ""

    if request.method == 'POST':
        create_form = CreateTaskForm(data=request.POST)
        if create_form.is_valid():
            task = create_form.save()
            task.save()
        else:
            err_task = create_form.errors
        return HttpResponseRedirect('task_list')
            
    context = {
        'task_list':task_list,
        'task_list1':task_list1,
        'task_list2':task_list2,
        'task_list3':task_list3,
        'create_form':create_form,
        'err_task':err_task,
    }
    return render(request, 'projets/task_list.html', context)


# mettre à jour une tâche

def edit_task(request, id_t):
    task = Tache.objects.get(id=id_t)
    if request.method == 'POST':
        create_form = CreateTaskForm(data=request.POST, instance=task)
        if create_form.is_valid():
            
            task = create_form.save(commit=False)
            
            progression = int(request.POST.get('progression'))
            if progression > 0 and progression < 100:
                task.etat = 'etat 2'
            elif progression == 100:
                task.etat =  'etat 3'

            task.save()
        else:
            err_task = create_form.errors
        return HttpResponseRedirect('../task_list')
    else:
        task_list = Tache.objects.all()
        task_list1 = Tache.objects.filter(etat='etat 1')
        task_list2 = Tache.objects.filter(etat='etat 2')
        task_list3 = Tache.objects.filter(etat='etat 3')

        create_form = CreateTaskForm(instance=task)
        err_task = ""
        edit = True
        context = {
            'task_list':task_list,
            'task_list1':task_list1,
            'task_list2':task_list2,
            'task_list3':task_list3,
            'create_form':create_form,
            'err_task':err_task,
            'edit':edit,
        }
        return render(request, 'projets/task_list.html', context)



# supprimer une tache

def delete_task(request, id_t):
    task = Tache.objects.get(id=id_t)
    task.delete()
    return HttpResponseRedirect('../task_list')


