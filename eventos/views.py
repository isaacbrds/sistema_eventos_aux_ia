from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Evento, Palestrante, Palestra, Participante, Participacao, Inscricao
from django.contrib import messages, auth
from django.contrib.messages import constants
from .forms import ParticipanteForm, PalestranteForm
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


def perfil_palestrante(request):
    palestrante = get_object_or_404(Palestrante, user=request.user)
    if request.method == 'POST':
        form = PalestranteForm(request.POST, instance=palestrante)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Parabéns, dados alterados com sucesso!')
            return redirect(reverse('lista_eventos'))
    else:
        form = PalestranteForm(instance=palestrante)
    return render(request, 'eventos/perfil_palestrante.html', {'form': form})

def login_palestrante(request):
    if request.method == 'GET':
        return render(request, 'eventos/login_palestrante.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário não encontrado')
            return redirect(reverse('login_palestrante'))

        auth.login(request, user)
        return redirect('/')

def cadastrar_palestrante(request):
    if request.method == 'GET':
        return render(request, 'eventos/cadastrar_palestrante.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        if password != password_confirmation:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect(reverse('cadastrar_palestrante'))

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Nome de usuário em uso')
            return redirect(reverse('cadastrar_palestrante'))

        user = User.objects.create_user(username=username, password=password)
        palestrante = Palestrante(user=user, nome_do_palestrante=username)
        palestrante.save()
        messages.add_message(request, constants.SUCCESS, 'Palestrante cadastrado com sucesso!')
        user.save()
        return redirect(reverse('login'))