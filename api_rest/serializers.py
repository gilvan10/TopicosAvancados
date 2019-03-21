from rest_framework import serializers
from clsapi import models

class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estabelecimento
        fields = ('id', 'descricao', 'localizacao',)
        depth = 1