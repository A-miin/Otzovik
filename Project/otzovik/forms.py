from django import forms

from otzovik.models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=('name', 'category', 'description', 'picture')