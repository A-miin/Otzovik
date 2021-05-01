from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import register_view, UserDetailView,UserChangeView


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('profile/update', UserChangeView.as_view(), name='profile-update'),
]