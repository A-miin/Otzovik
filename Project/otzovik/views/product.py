from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import reverse
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['reviews'] = self.object.review.all().exclude(is_moder=False)
        return context


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'otzovik.add_product'
    template_name = 'product/create.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('otzovik:product-list')

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'otzovik.change_product'
    form_class = ProductForm
    model = Product
    template_name = 'product/update.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('otzovik:product-view', kwargs={'pk':self.kwargs.get('pk')})

class ProductDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'otzovik.delete_product'
    template_name = 'product/delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('otzovik:product-list')


