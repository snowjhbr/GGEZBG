from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()  

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    data_de_aluguel = models.DateField(auto_now_add=True)
    data_de_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.jogo} alugado por {self.cliente}"