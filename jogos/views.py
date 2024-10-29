from django.shortcuts import render, redirect
from .models import Jogo
from .forms import JogoForm


def jogos(request):
    return render(request, 'jogos/index.html')  # Renderiza o template index.html
def index(request):
    return HttpResponse("Página inicial do app Jogos")

def listar_jogos(request):
    jogos = Jogo.objects.all() #Busca todos os jogos
    return render(request, 'jogos/index.html', {'jogos': jogos})

def cadastrar_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save() #Salva o jogo no banco de dados
            return redirect('listar_jogos') #Redireciona para a lista de jogos
    else:
        form = JogoForm()
    return render(request, 'jogos/cadastrar_jogo.html', {'form': form})