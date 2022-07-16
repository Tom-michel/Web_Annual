from django.urls import path
from .views import *

urlpatterns = [
    path('', accueil, name="accueil"),
    path('task_list', task_list, name="task_list"),
    path('edit_task/<str:id_t>', edit_task, name="edit_task"),
    path('edit_task_profile/<str:id_u>/<str:id_t>', edit_task_profile, name="edit_task_profile"),
    path('attrib_task/<str:id_t>', attrib_task, name="attrib_task"),
    path('remove_task/<str:id_t>/<str:m_id>', remove_task, name="remove_task"),
    path('delete_task/<str:id_t>', delete_task, name="delete_task"),
]