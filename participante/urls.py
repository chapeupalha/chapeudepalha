from django.urls import path

from .views import cadastro, novo_cadastro, cadastro_basico, cadastro_representante_legal, cadastro_documentos, \
    consultar_beneficiario, consultar_dados_beneficiario, cadastro_representante_legal_situacao, participante_cardsave

urlpatterns = [
    path('', cadastro, name='cadastro'),
    path('novo/', novo_cadastro, name='novo_cadastro'),
    path('cadastro/<int:id_participante>/', cadastro_basico, name='cadastro_basico'),
    path('cadastro/<int:id_participante>/representante', cadastro_representante_legal, name='cadastro_representante_legal'),
    path('cadastro/<int:id_participante>/representante/situacao/<int:status>', cadastro_representante_legal_situacao, name='cadastro_representante_legal_nao_possui'),
    path('cadastro/<int:id_participante>/documentos', cadastro_documentos, name='cadastro_documentos'),
    path('cadastro/<int:id_participante>/cardsave', participante_cardsave, name='participante_cardsave'),

    path('consultar/', consultar_beneficiario, name='consultar_beneficiario'),
    path('consulta/<int:id_participante>/', consultar_dados_beneficiario, name='consultar_dados_beneficiario'),

]


