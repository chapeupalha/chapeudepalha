from django.urls import path

from .views import *

urlpatterns = [
    path('', home_atividade, name='home_atividade'),
    path('cadastro/', cadastro_atividade, name='cadastro'),

    # path('cadastro/<int:id_participante>/', cadastro_basico, name='cadastro_basico'),

    path('ocorrencia/', home_ocorrencia, name='home_ocorrencia'),
    path('ocorrencia/nova/', cadastro_ocorrencia, name='cadastro_ocorrencia'),
    path('ocorrencia/<int:id_ocorrencia>/consulta', consulta_ocorrencia, name='consulta_ocorrencia'),
    path('ocorrencia/<int:id_ocorrencia>/solucao', solucao_ocorrencia, name='solucao_ocorrencia'),
    path('ocorrencia/<int:id_ocorrencia>/finalizar', finalizar_ocorrencia, name='finalizar_ocorrencia'),

    path('ocorrencia/ajax_marker_ocorrencia', ajax_marker_ocorrencia, name='ajax_marker_ocorrencia'),
    path('ajax_marker_atividade', ajax_marker_atividade, name='ajax_marker_atividade'),


]
