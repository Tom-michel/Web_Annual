from email.policy import default
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User

# Create your models here.



class Membre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='membre')
    photo = models.ImageField(default='pp.jpeg', blank=True)
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100, blank=True, default='fonction')
    description = models.TextField(max_length=500, blank=True, default='description')
    ROLES = (
        ('admin', 'admin'), ('membre', 'membre')
    )
    role = models.CharField(choices=ROLES, default='membre', blank=True, max_length=100)

    def __str__(self):
        return f'{self.user} Membre'
    
