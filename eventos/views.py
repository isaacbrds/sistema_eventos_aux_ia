from django.shortcuts import render, get_object_or_404
from .models import Evento
# Create your views here.

def lista_eventos(request):
    eventos = Evento.objects.all()
    contexto = {'eventos': eventos}
    return render(request,'eventos/lista_eventos.html', contexto)

def detalhe_evento(request, id=id):
    evento = get_object_or_404(Evento, pk=id)
    return render(request, 'eventos/detalhe_evento.html', { 'evento': evento })