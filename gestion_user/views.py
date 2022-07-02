from django.shortcuts import render

# Create your views here.


# page d'accueil

def index(request):
    return render(request, 'gestion_user/index.html')
