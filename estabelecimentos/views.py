from django.shortcuts import render, redirect
from .forms import EstabelecimentoForm

def cadastrar_estabelecimento(request):
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Namespace corrigido
            return redirect('estabelecimentos:login_estabelecimento')
    else:
        form = EstabelecimentoForm()
    return render(request, 'cadastrar_estabelecimento.html', {'form': form})
