from django.urls import path

from .views import *

urlpatterns = [
    path('', home_atividade, name='home_atividade'),
    path('cadastro/', cadastro, name='cadastro'),
    # path('cadastro/<int:id_participante>/', cadastro_basico, name='cadastro_basico'),

]
