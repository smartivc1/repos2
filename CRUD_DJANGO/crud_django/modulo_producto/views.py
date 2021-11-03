from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ProductoForm
from .models import Producto


class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm


class PagesListView(ListView):
    model = Producto

