from django.urls import path
from .views import *

urlpatterns = [
    path('', accueil, name="accueil"),
    path('task_list', task_list, name="task_list"),
]