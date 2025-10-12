from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import InstituicaoForm  # importa seu form

User = get_user_model()  # retorna seu modelo personalizado de usuário (Instituição)

# View de cadastro usando form
def cadastrar_instituicao(request):
    if request.method == 'POST':
        form = InstituicaoForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['senha'])  # define a senha corretamente
            usuario.save()
            messages.success(request, 'Instituição cadastrada com sucesso!')
            return redirect('instituicoes:login_instituicao')  # redireciona para login
        else:
            messages.error(request, 'Erro ao cadastrar instituição. Verifique os dados.')
    else:
        form = InstituicaoForm()

    return render(request, 'cadastrar_instituicao.html', {'form': form})

# Login da instituição
def login_instituicao(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = authenticate(request, username=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('instituicoes:perfil_instituicao')  # redireciona para perfil
        else:
            messages.error(request, 'Email ou senha incorretos')
    return render(request, 'login_instituicao.html')

# Perfil da instituição
def perfil_instituicao(request):
    return render(request, 'perfil_instituicao.html')

# Logout da instituição
def logout_instituicao(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta.")
    return redirect('instituicoes:login_instituicao')  # redireciona para login
