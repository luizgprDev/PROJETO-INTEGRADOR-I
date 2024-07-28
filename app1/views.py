from .forms import InsereRegistroForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Orcamento

class OrcamentoListView(ListView):
    template_name = "home.html"
    model = Orcamento
    context_object_name = 'clientes'

class OrcamentoCreateView(CreateView):
    template_name = "form_inserir.html"
    model = Orcamento
    form_class = InsereRegistroForm
    success_url = reverse_lazy("lista_clientes")

class OrcamentoUpdateView(UpdateView):
    template_name = "form_editar.html"
    model = Orcamento
    fields = '__all__'
    success_url = reverse_lazy("lista_clientes")

class OrcamentoDeleteView(DeleteView):
    template_name = "confirmar_exclusao.html"
    model = Orcamento
    success_url = reverse_lazy("lista_clientes")

# Create your views here.
