from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.OrcamentoListView.as_view(), name='lista_clientes'),
    path('inserir', views.OrcamentoCreateView.as_view(), name='inserir'),
    path('editar/<int:pk>', views.OrcamentoUpdateView.as_view(), name= 'editar'),
    path( 'excluir/<int:pk>' , views.AgendaDeleteView.as_view(), name= 'excluir')
]