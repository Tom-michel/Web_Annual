from django.contrib import admin
from .models import Tache

# Register your models here.


class AdminTache(admin.ModelAdmin):
	list_display   = ('id', 'etat', 'created', 'updated', 'intitule',)
	list_filter    = ('etat',)
	search_fields  = ('etat', 'intitule', 'membres',)
admin.site.register(Tache, AdminTache)