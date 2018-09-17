from django.contrib import admin


from atividade.models import Equipe_trabalho, Unidade_gestora, Tipo_atividade, Trabalho_campo


class EquipeTrabalho(admin.ModelAdmin):
    models = Equipe_trabalho
    list_display = ('nome', 'descricao',)


class UnidadeGestora(admin.ModelAdmin):
    models = Unidade_gestora
    list_display = ('nome', 'descricao',)


class TipoAtividade(admin.ModelAdmin):
    models = Tipo_atividade
    list_display = ('nome', 'descricao', 'categoria',)


class TrabalhoCampo(admin.ModelAdmin):
    models = Trabalho_campo
    list_display = ('nome', 'descricao',)

admin.site.register(Equipe_trabalho, EquipeTrabalho)
admin.site.register(Unidade_gestora, UnidadeGestora)
admin.site.register(Tipo_atividade, TipoAtividade)
admin.site.register(Trabalho_campo, TrabalhoCampo)