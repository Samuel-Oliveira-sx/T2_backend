from django.db import models
from django.shortcuts import render

# Modelo para posts
class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Modelo para quarto
class Quarto(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"Quarto {self.numero} - {self.tipo}"

# Modelo para cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

# Modelo para reserva
class Reserva(models.Model):
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_entrada = models.DateField()
    data_saida = models.DateField()
    status = models.CharField(max_length=20, choices=[('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')])

    def __str__(self):
        return f"Reserva para {self.cliente} no quarto {self.quarto.numero}"


