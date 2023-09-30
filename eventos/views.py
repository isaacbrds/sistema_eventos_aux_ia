from django.shortcuts import render, get_object_or_404
from .models import Evento, Palestrante, Palestra
# Create your views here.


def lista_eventos(request):
    eventos = Evento.objects.all()
    contexto = {'eventos': eventos}
    return render(request,'eventos/lista_eventos.html', contexto)


def detalhe_evento(request, id=id):
    evento = get_object_or_404(Evento, pk=id)
    palestrantes_do_evento = Palestrante.objects.filter(evento=evento)
    palestras_do_evento = Palestra.objects.filter(palestrante__in=palestrantes_do_evento)
    return render(request, 'eventos/detalhe_evento.html', { 'evento': evento, 'palestrantes': palestrantes_do_evento, 'palestras': palestras_do_evento })


def detalhe_palestrante(request, id=id):
    palestrante = get_object_or_404(Palestrante, pk=id)
    palestras = palestrante.palestra_set.all()
    return render(request, 'eventos/detalhe_palestrante.html', { 'palestrante': palestrante, 'palestras': palestras})