from django.contrib import admin
from .models import Tache, Projet

# Register your models here.


class AdminTache(admin.ModelAdmin):
	list_display   = ('id', 'etat', 'created', 'updated', 'intitule',)
	list_filter    = ('etat',)
	search_fields  = ('etat', 'intitule', 'membres',)
admin.site.register(Tache, AdminTache)


class AdminProjet(admin.ModelAdmin):
	list_display   = ('id', 'titre', 'created', 'updated',)
	list_filter    = ('titre', 'created',)
	search_fields  = ('titre',)
admin.site.register(Projet, AdminProjet)

