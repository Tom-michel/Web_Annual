from django.urls import path
from .views import *

urlpatterns = [
    path('index', index, name="index"),
    path('connexion', connexion, name="connexion"),
    path('inscription', inscription, name="inscription"),
    path('member_list', member_list, name='member_list'),
    path('profil_membre/<str:id_u>', profil_membre, name="profil_membre"),
    path('supprimer_compte/<str:id_u>', supprimer_compte, name="supprimer_compte"),
    path('supprimer_compte_2/<str:id_u>', supprimer_compte_2, name="supprimer_compte_2"),
    path('logout', user_logout, name='user_logout'),
]