from django.contrib import admin
from .models import Evento, Participante, Palestrante, Ingresso, Palestra, Inscricao, Participacao
# Register your models here.

admin.site.register(Evento)
admin.site.register(Palestrante)
admin.site.register(Participacao)
admin.site.register(Palestra)
admin.site.register(Participante)
admin.site.register(Inscricao)
admin.site.register(Ingresso)