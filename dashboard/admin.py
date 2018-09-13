from django.contrib import admin

from dashboard.models import Documento


class docAdmin(admin.ModelAdmin):
    models = Documento
    list_display = ('foto_perfil',)

admin.site.register(Documento, docAdmin)