from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from .managers import *
import uuid


class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)  

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
    
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(unique = True, blank = False)
    name = models.CharField(max_length = 256)
    sector = models.CharField(max_length=64, choices=sectorCompleteChoices, default='A')

    groups = models.ManyToManyField(
        Group,
        related_name='user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions',
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.name
    
    @property
    def user_image(self):
        if " " in self.name:
           name = self.name.split(" ")
        else: name = self.name

        firstName = name[0]
        secondName = name[1]
        
        return firstName[0].upper() + secondName[0].upper()