from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EstabelecimentoForm
from .models import Estabelecimento
from django.contrib.auth import authenticate, login, logout

def cadastrar_estabelecimento(request):
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('estabelecimentos:login_estabelecimento')
    else:
        form = EstabelecimentoForm()
    # Ajuste: removido o prefixo 'estabelecimentos/' para buscar direto na pasta templates do app
    return render(request, 'cadastrar_estabelecimento.html', {'form': form})


def login_estabelecimento(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, email=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('estabelecimentos:perfil_estabelecimento')
        else:
            messages.error(request, 'Email ou senha incorretos.')
    # Ajuste: removido o prefixo 'estabelecimentos/'
    return render(request, 'login_estabelecimento.html')


def perfil_estabelecimento(request):
    if not request.user.is_authenticated:
        return redirect('estabelecimentos:login_estabelecimento')
    # Ajuste: removido o prefixo 'estabelecimentos/'
    return render(request, 'perfil_estabelecimento.html', {'estabelecimento': request.user})


def logout_estabelecimento(request):
    logout(request)
    return redirect('estabelecimentos:login_estabelecimento')
