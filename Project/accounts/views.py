from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator

from django.views.generic import DetailView, ListView, UpdateView
from .forms import UserRegisterForm, UserChangeForm, PasswordUpdateForm


def register_view(request, *args, **kwargs):
    if request.method=='POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('otzovik:product-list')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/create.html', context={'form':form})

class UserDetailView(DetailView):

    model = get_user_model()
    template_name = 'detail.html'
    context_object_name = 'user_object'



class UserChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'update.html'
    context_object_name = 'user_object'

    def get_object(self, queryset=None):
        self.object = self.request.user
        return self.object

    def get_success_url(self):
        return reverse('accounts:profile')


class UserPasswordUpdateView(LoginRequiredMixin,UpdateView):
    model = get_user_model()
    template_name = 'password.html'
    form_class = PasswordUpdateForm
    context_object_name = 'user_object'

    def get_success_url(self):
        return reverse('accounts:login')
    def get_object(self, queryset=None):
        return self.request.user