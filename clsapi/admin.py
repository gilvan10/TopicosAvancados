from django.contrib import admin
from .models import Estabelecimento
from .models import Marca
from .models import Unidade
from .models import Filtro

admin.site.register(Estabelecimento)
admin.site.register(Marca)
admin.site.register(Unidade)
admin.site.register(Filtro)
