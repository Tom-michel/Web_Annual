from django.contrib import admin
from .models import Membre

# Register your models here.

class AdminMembre(admin.ModelAdmin):
	list_display   = ('user', 'fonction', 'ville', 'quartier', 'telephone')
	list_filter    = ('fonction', 'ville', 'quartier',)
	search_fields  = ('fonction', 'ville', 'quartier',)
admin.site.register(Membre, AdminMembre)