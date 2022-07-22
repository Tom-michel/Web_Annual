from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils import timezone

from gestion_user.models import Membre

# Create your models here.


class Tache(models.Model):
    ETATS = (
        ('etat 1','etat1'),('etat 2','etat2'),('etat 3','etat3')
    )
    etat = models.CharField(max_length=20, choices=ETATS, default='etat 1')
    intitule = models.CharField(max_length=100)
    progression = models.IntegerField(default=0)
    membres = models.ManyToManyField(Membre)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Projet(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, default='Brève description du projet')
    membres = models.ManyToManyField(Membre)
    taches = models.ManyToManyField(Tache)
    progression = models.IntegerField(default=0)
    VIS = (('public','public'), ('private','private'))
    visibilite = models.CharField(max_length=200, choices=VIS, default='public')
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(default=timezone.now, blank=True)


