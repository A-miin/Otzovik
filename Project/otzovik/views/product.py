from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from otzovik.models import Product
from otzovik.forms import ProductForm

class IndexView(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'

class ProductView(DetailView):
    model = Product
    template_name = 'product/view.html'
    context_object_name = 'product'

class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'otzovik.add_product'
    template_name = 'product/create.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('otzovik:product-list')

