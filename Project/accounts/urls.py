from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import register_view


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
]