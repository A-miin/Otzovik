from django.urls import path
from otzovik.views import IndexView

app_name='otzovik'
urlpatterns=[
    path('', IndexView.as_view(), name='product-list'),


]