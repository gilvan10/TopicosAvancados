from django.urls import path
from . import views

urlpatterns = [
path('index', views.index, name='index'),
path('', views.estabelecimento, name='estabelecimento'),
path('estabelecimento/<int:pk>/', views.estabelecimento_detail, name='estabelecimento_detail'),
path('', views.marca, name='marca'),
path('marca/<int:pk>/', views.marca_detail, name='marca_detail'),
path('', views.unidade, name='unidade'),
path('unidade/<int:pk>/', views.unidade_detail, name='unidade_detail'),
path('', views.filtro, name='filtro'),
path('filtro/<int:pk>/', views.filtro_detail, name='filtro_detail'),
]