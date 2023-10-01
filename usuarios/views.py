from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário não encontrado')
            return redirect(reverse('login'))

        auth.login(request, user)
        return redirect('/eventos/')

def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))


def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastrar.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        if password != password_confirmation:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect(reverse('cadastrar'))

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Nome de usuário em uso')
            return redirect(reverse('cadastrar'))

        user = User.objects.create_user(username=username, password=password)
        messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
        user.save()
        return redirect(reverse('login'))