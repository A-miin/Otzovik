from django.urls import path
from otzovik.views import IndexView, ProductView, ProductCreateView

app_name='otzovik'
urlpatterns=[
    path('', IndexView.as_view(), name='product-list'),
    path('<int:pk>', ProductView.as_view(), name='product-view'),
    path('create/', ProductCreateView.as_view(), name='product-create'),


]