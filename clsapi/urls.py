from django.urls import path
from . import views

urlpatterns = [
path('index', views.index, name='index'),
path('estabelecimento/new', views.estabelecimento_new, name='estabelecimento_new'),
path('filtro/new', views.filtro_new, name='filtro_new'),
path('marca/new', views.marca_new, name='marca_new'),
path('unidade/new', views.unidade_new, name='unidade_new'),
path('', views.estabelecimento, name='estabelecimento'),
path('estabelecimento/<int:pk>/', views.estabelecimento_detail, name='estabelecimento_detail'),
path('', views.marca, name='marca'),
path('marca/<int:pk>/', views.marca_detail, name='marca_detail'),
path('', views.unidade, name='unidade'),
path('unidade/<int:pk>/', views.unidade_detail, name='unidade_detail'),
path('', views.filtro, name='filtro'),
path('filtro/<int:pk>/', views.filtro_detail, name='filtro_detail'),
path('estabelecimento/<int:pk>/edit/', views.estabelecimento_edit, name='estabelecimento_edit'),
path('filtro/<int:pk>/edit/', views.filtro_edit, name='filtro_edit'),
path('marca/<int:pk>/edit/', views.marca_edit, name='marca_edit'),
path('unidade/<int:pk>/edit/', views.unidade_edit, name='unidade_edit'),
path('estabelecimento/<int:pk>/delete/', views.estabelecimento_delete, name='estabelecimento_delete'),
path('filtro/<int:pk>/delete/', views.filtro_delete, name='filtro_delete'),
path('marca/<int:pk>/delete/', views.marca_delete, name='marca_delete'),
path('unidade/<int:pk>/delete/', views.unidade_delete, name='unidade_delete'),
]