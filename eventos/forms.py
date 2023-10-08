from django.forms import ModelForm
from .models import Participante, Palestrante
class ParticipanteForm(ModelForm):
    class Meta:
        model = Participante
        fields = ['nome_do_participante', 'email', 'numero_telefone', 'informacoes_adicionais']


class PalestranteForm(ModelForm):
    class Meta:
        model = Palestrante
        fields = ['nome_do_palestrante', 'resumo_do_palestrante' ]
