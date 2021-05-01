from django import forms

from otzovik.models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=('name', 'category', 'description', 'picture')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'rate' )

class ReviewModerForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'rate', 'is_moder' )
