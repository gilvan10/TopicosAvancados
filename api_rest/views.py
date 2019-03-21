from django.shortcuts import render
from clsapi import models
from api_rest import serializers
from rest_framework import generics

# Create your views here.

class EstabelecimentoListServiceView(generics.ListCreateAPIView):
    queryset = models.Estabelecimento.objects.all()
    serializer_class = serializers.EstabelecimentoSerializer
