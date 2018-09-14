from django.urls import path

from .views import cadastro, novo_cadastro, cadastro_basico, cadastro_representante_legal, cadastro_documentos, \
    consultar_beneficiario, consultar_dados_beneficiario

urlpatterns = [
    path('', cadastro, name='cadastro'),
    path('novo/', novo_cadastro, name='novo_cadastro'),
    path('cadastro/<int:id_participante>/', cadastro_basico, name='cadastro_basico'),
    path('cadastro/<int:id_participante>/representante', cadastro_representante_legal, name='cadastro_representante_legal'),
    path('cadastro/<int:id_participante>/documentos', cadastro_documentos, name='cadastro_documentos'),

    path('consultar/', consultar_beneficiario, name='consultar_beneficiario'),
    path('consulta/<int:id_participante>/', consultar_dados_beneficiario, name='consultar_dados_beneficiario'),

]
