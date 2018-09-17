from django.contrib import admin
from core.models import Municipio


class MunicipioChapeu(admin.ModelAdmin):
    models = Municipio
    list_display = ('nome', 'uf',)

admin.site.register(Municipio, MunicipioChapeu)