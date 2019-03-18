from django.urls import path
from . import views

urlpatterns = [
path('index', views.index, name='index'),
path('', views.estabelecimento, name='estabelecimento'),
path('', views.marca, name='marca'),
path('', views.unidade, name='unidade'),
path('', views.filtro, name='filtro'),
]