from django import forms
from .models import Quarto, Cliente, Reserva

class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = ['numero', 'tipo', 'preco', 'descricao', 'disponivel']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['quarto', 'cliente', 'data_entrada', 'data_saida', 'status']
