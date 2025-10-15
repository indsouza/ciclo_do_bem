from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EstabelecimentoForm
from django.contrib.auth import authenticate, login, logout

def cadastrar_estabelecimento(request):
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST, request.FILES)
        senha = request.POST.get('senha')
        confirm_senha = request.POST.get('confirm_senha')

        if senha != confirm_senha:
            messages.error(request, 'As senhas não coincidem.')
        elif form.is_valid():
            estabelecimento = form.save(commit=False)
            estabelecimento.set_password(senha)
            estabelecimento.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('estabelecimentos:login_estabelecimento')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = EstabelecimentoForm()

    return render(request, 'cadastrar_estabelecimento.html', {
        'form': form,
    })


def login_estabelecimento(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, email=email, password=senha)
        if user:
            login(request, user)
            return redirect('estabelecimentos:perfil_estabelecimento')
        else:
            messages.error(request, 'Email ou senha incorretos.')
    return render(request, 'login_estabelecimento.html')


def perfil_estabelecimento(request):
    if not request.user.is_authenticated:
        return redirect('estabelecimentos:login_estabelecimento')
    return render(request, 'perfil_estabelecimento.html', {'estabelecimento': request.user})


def logout_estabelecimento(request):
    logout(request)
    return redirect('estabelecimentos:login_estabelecimento')
