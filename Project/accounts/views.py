from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator

from django.views.generic import DetailView, ListView, UpdateView
from .forms import UserRegisterForm


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