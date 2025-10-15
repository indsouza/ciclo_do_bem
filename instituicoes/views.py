from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InstituicaoForm
from .models import Instituicao
from django.contrib.auth import authenticate, login, logout

# View de cadastro usando form
def cadastrar_instituicao(request):
    if request.method == 'POST':
        form = InstituicaoForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save(commit=False)
            # Salva a senha de forma segura usando set_password do AbstractBaseUser
            usuario.set_password(form.cleaned_data['senha'])
            usuario.save()
            messages.success(request, 'Instituição cadastrada com sucesso!')
            return redirect('instituicoes:login_instituicao')
        else:
            # Mostra os erros detalhados do form
            messages.error(request, f'Erro ao cadastrar instituição: {form.errors}')
    else:
        form = InstituicaoForm()

    return render(request, 'cadastrar_instituicao.html', {'form': form})


# Login simples da instituição (sem Django auth completo)
def login_instituicao(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Instituicao.objects.get(email=email)
            # Usando check_password do AbstractBaseUser
            if usuario.check_password(senha):
                # Guarda o ID da instituição na sessão
                request.session['instituicao_id'] = usuario.id
                request.session['instituicao_nome'] = usuario.nome_fantasia
                messages.success(request, f"Bem-vindo, {usuario.nome_fantasia}!")
                return redirect('instituicoes:perfil_instituicao')
            else:
                messages.error(request, 'Senha incorreta.')
        except Instituicao.DoesNotExist:
            messages.error(request, 'Instituição não encontrada.')

    return render(request, 'login_instituicao.html')


# Perfil da instituição (requer sessão ativa)
def perfil_instituicao(request):
    instituicao_id = request.session.get('instituicao_id')
    if not instituicao_id:
        messages.warning(request, "Você precisa estar logado para acessar o perfil.")
        return redirect('instituicoes:login_instituicao')

    instituicao = Instituicao.objects.get(id=instituicao_id)
    return render(request, 'perfil_instituicao.html', {'instituicao': instituicao})


# Logout simples
def logout_instituicao(request):
    request.session.flush()  # limpa a sessão
    messages.success(request, "Você saiu da sua conta.")
    return redirect('instituicoes:login_instituicao')
