from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

from gestion_user.models import Membre

# Create your models here.


class Tache(models.Model):
    ETATS = (
        ('etat 1','etat1'),('etat 2','etat2'),('etat 3','etat3')
    )
    etat = models.CharField(max_length=20, choices=ETATS)
    intitule = models.CharField(max_length=100)
    progression = models.IntegerField()
    membres = models.ManyToManyField(Membre)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)