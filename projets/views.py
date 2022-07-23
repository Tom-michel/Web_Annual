from multiprocessing import context
from re import A
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from gestion_user.models import Membre
from .models import Tache, Projet
from .forms import CreateTaskForm, CreateProjectForm, EditProjectForm
from gestion_user.views import connexion, member_list

# Create your views here.


# page d'accueil

# @login_required(login_url='index')
def accueil(request):
    if request.user.is_authenticated:
        project_form = CreateProjectForm()
        err_proj = ""
        if request.method == "POST":
            project_form = CreateProjectForm(data=request.POST)
            if project_form.is_valid():
                project = project_form.save()

                if project.taches.all():
                    n,s = 0,0
                    for task in project.taches.all():
                        s += task.progression
                        n += 1
                    project.progression = s/n
                project.save()
                return projet(request, project.id)
            else:
                err_proj = project_form.errors
                return HttpResponseRedirect('accueil')
        else:
            projets = Projet.objects.all()
            private_proj = []
            public_proj = []
            for p in projets:
                if p.visibilite == 'public':
                    public_proj.append(p)
                elif p.visibilite == 'private':
                    private_proj.append(p)

            context = {
                'projets':projets,
                'private_proj':private_proj,
                'public_proj':public_proj,
                'project_form':project_form,
                'err_proj':err_proj,
            }
            return render(request, 'projets/accueil.html', context)
    else:
        return render(request, 'gestion_user/index.html')




# page de gestion d'un projet

def projet(request, id_p):
    context = {
        'id_p':id_p,
    }
    return render(request, 'projets/projet.html', context)




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
            else:
                task.etat =  'etat 1'
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



# attribuer une tâche à un membre

def attrib_task(request, id_t):
    task = Tache.objects.get(id=id_t)
    if request.method == 'POST':
        listAttrib = request.POST.get('valAttrib')
        valAttrib = listAttrib.split(',')
        for m_id in valAttrib:
            member = Membre.objects.get(id=m_id)
            task.membres.add(member)
        return HttpResponseRedirect('../task_list')
        # context = {'valAttrib':valAttrib}
        # return render(request, 'projets/task_list.html', context)
    else:
        task_list1 = Tache.objects.filter(etat='etat 1')
        task_list2 = Tache.objects.filter(etat='etat 2')
        task_list3 = Tache.objects.filter(etat='etat 3')
        attrib = True
        err_task = ""
        edit = False

        member_list = []
        for member in Membre.objects.all():
            if not member in task.membres.all():
                member_list.append(member)
        context = {
            'task_list1':task_list1,
            'task_list2':task_list2,
            'task_list3':task_list3,
            'attrib':attrib,
            'err_task':err_task,
            'edit':edit,
        
            'member_list':member_list,
            'task':task,
        }
        return render(request, 'projets/task_list.html', context)
        # return HttpResponseRedirect('../task_list')



# desattribuer une tâche

def remove_task(request, id_t, m_id):
    task = Tache.objects.get(id=id_t)
    member = Membre.objects.get(id=m_id)
    task.membres.remove(member)
    return HttpResponseRedirect('../../task_list')


