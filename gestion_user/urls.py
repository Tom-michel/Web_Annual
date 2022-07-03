from django.urls import path
from .views import *

urlpatterns = [
    path('index', index, name="index"),
    path('connexion', connexion, name="connexion"),
    path('inscription', inscription, name="inscription"),
    path('logout', user_logout, name='user_logout'),
]