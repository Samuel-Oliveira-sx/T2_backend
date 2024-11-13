from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_quartos, name='listar_quartos'),
    path('quarto/novo/', views.criar_quarto, name='criar_quarto'),
    path('quarto/editar/<int:pk>/', views.editar_quarto, name='editar_quarto'),
    path('quarto/deletar/<int:pk>/', views.deletar_quarto, name='deletar_quarto'),
    path('cliente/novo/', views.criar_cliente, name='criar_cliente'),
    path('reserva/novo/', views.criar_reserva, name='criar_reserva'),
    path('reservas/', views.listar_reservas, name='listar_reservas'),  # Adicione esta linha
    path('reserva/cancelar/<int:pk>/', views.cancelar_reserva, name='cancelar_reserva'),
]
