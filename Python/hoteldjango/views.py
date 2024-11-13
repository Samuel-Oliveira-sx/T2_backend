from django.shortcuts import render, redirect, get_object_or_404
from .models import Quarto, Cliente, Reserva
from .forms import QuartoForm, ClienteForm, ReservaForm

# Listar quartos
def listar_quartos(request):
    quartos = Quarto.objects.all()
    return render(request, 'hoteldjango/listar_quartos.html', {'quartos': quartos})

# Criar um novo quarto
def criar_quarto(request):
    if request.method == 'POST':
        form = QuartoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_quartos')
    else:
        form = QuartoForm()
    return render(request, 'hoteldjango/criar_quartos.html', {'form': form})

# Editar um quarto
def editar_quarto(request, pk):
    quarto = Quarto.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuartoForm(request.POST, instance=quarto)
        if form.is_valid():
            form.save()
            return redirect('listar_quartos')
    else:
        form = QuartoForm(instance=quarto)
    return render(request, 'hoteldjango/editar_quarto.html', {'form': form})

# Deletar um quarto
def deletar_quarto(request, pk):
    quarto = Quarto.objects.get(pk=pk)
    if request.method == 'POST':
        quarto.delete()
        return redirect('listar_quartos')
    return render(request, 'hoteldjango/deletar_quarto.html', {'quarto': quarto})

# Criar um novo cliente
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_quartos')
    else:
        form = ClienteForm()
    return render(request, 'hoteldjango/criar_cliente.html', {'form': form})

# Criar uma nova reserva
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_quartos')
    else:
        form = ReservaForm()
    return render(request, 'hoteldjango/criar_reserva.html', {'form': form})

def cancelar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)  # Busca a reserva ou retorna 404 se não existir
    if request.method == 'POST':
        reserva.status = 'Cancelada'  # Altera o status da reserva para "Cancelada"
        reserva.save()  # Salva a alteração no banco de dados
        return redirect('listar_reservas')  # Redireciona para a lista de reservas
    return render(request, 'hoteldjango/cancelar_reserva.html', {'reserva': reserva})

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'hoteldjango/listar_reservas.html', {'reservas': reservas})