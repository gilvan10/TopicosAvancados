from django import forms
from .models import Estabelecimento

class EstabelecimentoForm(forms.ModelForm):

    class Meta:
        model = Estabelecimento
        fields = ('id', 'descricao', 'localizacao',)