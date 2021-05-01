
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from otzovik.models import Product

class IndexView(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'
