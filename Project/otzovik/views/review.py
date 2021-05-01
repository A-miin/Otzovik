from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import reverse, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from otzovik.models import Review, Product
from otzovik.forms import ReviewForm, ReviewModerForm

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

class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'otzovik.change_review'
    def has_permission(self):
        review = get_object_or_404(Review, id=self.kwargs.get('pk'))
        return super().has_permission() or (self.request.user==review.author)

    form_class = ReviewForm
    model = Review
    template_name = 'review/update.html'
    context_object_name = 'product'

    def get_form_class(self):
        if self.request.user.groups.filter(name='Moderator').exists():
            self.form_class = ReviewModerForm
        return super().get_form_class()

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        if not self.request.user.groups.filter(name='Moderator').exists():
            self.object.is_moder=False

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('otzovik:product-view', kwargs={'pk':self.object.product.id})
