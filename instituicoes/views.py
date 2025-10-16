from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InstituicaoForm
from django.contrib.auth import authenticate, login, logout
from .models import Instituicao

def cadastrar_instituicao(request):
    if request.method == 'POST':
        form = InstituicaoForm(request.POST, request.FILES)
        senha = request.POST.get('senha')
        confirm_senha = request.POST.get('confirm_senha')

        if senha != confirm_senha:
            messages.error(request, 'As senhas não coincidem.')
        elif form.is_valid():
            instituicao = form.save(commit=False)
            instituicao.set_password(senha)
            instituicao.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('instituicoes:login_instituicao')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = InstituicaoForm()

    return render(request, 'cadastrar_instituicao.html', {'form': form})


def login_instituicao(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, email=email, password=senha)

        if user:
            login(request, user)
            # Seta a variável de sessão para identificar que é instituição
            request.session['instituicao_id'] = user.id
            return redirect('instituicoes:perfil_instituicao')
        else:
            messages.error(request, 'Email ou senha incorretos.')

    return render(request, 'login_instituicao.html')



def perfil_instituicao(request):
    if not request.user.is_authenticated:
        return redirect('instituicoes:login_instituicao')
    return render(request, 'perfil_instituicao.html', {'instituicao': request.user})


def logout_instituicao(request):
    logout(request)
    if 'instituicao_id' in request.session:
        del request.session['instituicao_id']
    return redirect('instituicoes:login_instituicao')
