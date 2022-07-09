from django.urls import path
from .views import *

urlpatterns = [
    path('', accueil, name="accueil"),
    path('task_list', task_list, name="task_list"),
    path('edit_task/<str:id_t>', edit_task, name="edit_task"),
    path('delete_task/<str:id_t>', delete_task, name="delete_task"),
]