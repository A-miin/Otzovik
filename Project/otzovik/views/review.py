from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from otzovik.models import Review, Product
from otzovik.forms import ReviewForm

class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = 'review/create.html'
    form_class = ReviewForm
    model = Review

    def get(self,request, *args, **kwargs):
        self.kwargs['product']=kwargs.get('pk')
        self.object=None
        return super().get(request, *args, **kwargs)


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.product = Product.objects.get(pk=self.kwargs.get('pk'))
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('otzovik:product-view', kwargs={'pk':self.kwargs.get('pk')})


