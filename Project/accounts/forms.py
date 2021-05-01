from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        fields=['username', 'first_name']
