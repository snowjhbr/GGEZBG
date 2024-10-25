from django.shortcuts import render
from django.http import HttpResponse

def jogos(request):
    return render(request, 'jogos/index.html')  # Renderiza o template index.html
def index(request):
    return HttpResponse("Página inicial do app Jogos")
