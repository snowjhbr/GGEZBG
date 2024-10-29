from django import forms
from .models import Jogo, Cliente, Aluguel

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome', 'descricao', 'preco', 'estoque']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ['cliente', 'jogo', 'data_de_devolucao']
