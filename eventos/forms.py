from django.forms import ModelForm
from .models import Participante
class ParticipanteForm(ModelForm):
    class Meta:
        model = Participante
        fields = ['nome_do_participante', 'email', 'numero_telefone', 'informacoes_adicionais']
