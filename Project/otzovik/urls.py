from django.urls import path
from otzovik.views import (IndexView, ProductView, ProductCreateView, ProductDeleteView,ProductUpdateView,
                           ReviewCreateView,ReviewUpdateView,ReviewDeleteView)

app_name='otzovik'
urlpatterns=[
    path('', IndexView.as_view(), name='product-list'),
    path('<int:pk>', ProductView.as_view(), name='product-view'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/edit', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('<int:pk>/review/create', ReviewCreateView.as_view(), name = 'review-create'),
    path('<int:pk>/review/update', ReviewUpdateView.as_view(), name = 'review-update'),
    path('<int:pk>/review/delete', ReviewDeleteView.as_view(), name = 'review-delete'),


]