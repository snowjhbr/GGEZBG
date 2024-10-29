from django.urls import path
from . import views
from .views import listar_jogos, cadastrar_jogo


urlpatterns = [
    path('', views.index, name='index'),  # Define a rota para a página inicial do app 'jogos'
    path('', listar_jogos, name='listar_jogos'), #página inicial
    path('cadastrar/', cadastrar_jogo, name='cadastrar_jogo'), #página de cadastro
]
