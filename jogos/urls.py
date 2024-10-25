from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a rota para a página inicial do app 'jogos'
]
