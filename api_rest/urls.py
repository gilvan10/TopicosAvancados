from api_rest import views
from django.urls import path

urlpatterns = [
path('estabelecimentos/', views.EstabelecimentoListServiceView.as_view(), name='estabelecimentos'),
]