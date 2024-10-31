from django.urls import path
from . import views
from .views import listar_jogos, cadastrar_jogo
from .views import *


urlpatterns = [
    path('', views.index, name='index'),  # Define a rota para a página inicial do app 'jogos'
    path('', listar_jogos, name='listar_jogos'), #página inicial
    path('cadastrar/', cadastrar_jogo, name='cadastrar_jogo'), #página de cadastro
    path('login/', Login.as_view(), name='login'), #página de login
    path('logout/', Logout.as_view(), name='logout'), #página de logout
    path('cadastro/', RegisterUser.as_view(), name='register'), #página de cadastro de usuário
    path('usuarios/', Users.as_view(), name='users'), #página visualização de usuários
    path('paginaUsuario/<str:id>', ViewUserProfile.as_view(), name='user_page'),
    path('', Redirect.as_view(), name=''),
    path('perfil/', ViewUserProfile.as_view(), name='user_profile'), #página de perfil

]
