from django.shortcuts import render, redirect
from .forms import EstabelecimentoForm
from .models import Estabelecimento

def cadastrar_estabelecimento(request):
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            senha = dados.pop('senha')
            estabelecimento = Estabelecimento.objects.create_user(
                email=dados['email'],
                senha=senha,
                **{k: v for k, v in dados.items() if k != 'email'}
            )
            return redirect('login_estabelecimento')  # nome da rota que leva ao login
    else:
        form = EstabelecimentoForm()
    return render(request, 'cadastrar_estabelecimento.html', {'form': form})
