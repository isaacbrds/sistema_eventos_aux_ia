from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Evento, Palestrante, Palestra, Participante, Participacao, Inscricao
from django.contrib import messages, auth
from django.contrib.messages import constants
from .forms import ParticipanteForm
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

def detalhe_palestra(request, id=id):
    palestra = get_object_or_404(Palestra, pk=id)
    return render(request, 'eventos/detalhe_palestra.html', { 'palestra': palestra})


@login_required
def participar_evento(request, id=id):
    evento = get_object_or_404(Evento, pk=id)
    if request.method == 'GET':
        return render(request, 'eventos/participacao_evento.html', {'evento': evento})
    elif request.method == 'POST':
        if request.user.is_authenticated:
            #participante = Participante.objects.filter(user=request.user).first()
            participante = get_object_or_404(Participante, user=request.user)

            # Certifique-se de que o participante existe antes de criar a inscrição
            if participante:
                participacao = Participacao(evento=evento, participante=participante)
                participacao.save()

                messages.add_message(request, constants.SUCCESS, 'Parabéns, você está inscrito.')
                return redirect(reverse('detalhe_evento', kwargs={'id': id}))
            else:
                messages.add_message(request, constants.ERROR, 'Você não é um participante válido.')
                return redirect(reverse('detalhe_evento', kwargs={'id': id}))
        else:
            messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para se inscrever.')
            return redirect(reverse('detalhe_evento', kwargs={'id': id}))

def inscrever_palestra(request, id=id):
    palestra = get_object_or_404(Palestra, pk=id)
    if request.method == 'GET':
        return render(request, 'eventos/inscricao_palestra.html', {'palestra': palestra})
    elif request.method == 'POST':
        if request.user.is_authenticated:
#            participante = Participante.objects.filter(user=request.user).first()
            participante = get_object_or_404(Participante, user=request.user)

            # Certifique-se de que o participante existe antes de criar a inscrição
            if participante:
                participante_ja_inscrito = Inscricao.objects.filter(palestra=palestra, participante=participante, evento=palestra.palestrante.evento)

                if participante_ja_inscrito:
                    messages.add_message(request, constants.ERROR, 'você já está inscrito nessa palestra.')
                else:
                    inscricao = Inscricao(evento=palestra.palestrante.evento, participante=participante, palestra=palestra)
                    inscricao.save()
                    messages.add_message(request, constants.SUCCESS, 'Parabéns, você está inscrito nessa palestra.')

                return redirect(reverse('detalhe_palestra', kwargs={'id': id}))
            else:
                messages.add_message(request, constants.ERROR, 'Você não é um participante válido.')
                return redirect(reverse('detalhe_palestra', kwargs={'id': id}))
        else:
            messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para se inscrever.')
            return redirect(reverse('detalhe_palestra', kwargs={'id': id}))

def perfil_participante(request):
    participante = get_object_or_404(Participante, user=request.user)
    if request.method == 'POST':
        form = ParticipanteForm(request.POST, instance=participante)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Parabéns, dados alterados com sucesso!')
            return redirect(reverse('lista_eventos'))
    else:
        form = ParticipanteForm(instance=participante)
    return render(request, 'eventos/perfil_participante.html', {'form': form})
