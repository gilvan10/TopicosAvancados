from django import forms
from .models import Filtro

class FiltroForm(forms.ModelForm):

    class Meta:
        model = Filtro
        fields = ('id', 'descricao',)