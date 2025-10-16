from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Oferta, Reserva
from .forms import OfertaForm
from django.db.models import Q
from datetime import datetime
from .decorators import estabelecimento_required, instituicao_required

# ============================
# ESTABELECIMENTO VIEWS
# ============================

@login_required
@estabelecimento_required
def criar_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST, request.FILES)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.estabelecimento = request.user
            oferta.save()
            messages.success(request, "Oferta criada com sucesso!")
            return redirect('ofertas:minhas_ofertas')
    else:
        form = OfertaForm()
    return render(request, 'ofertas/criar_oferta.html', {'form': form})

@login_required
@estabelecimento_required
def minhas_ofertas(request):
    ofertas = Oferta.objects.filter(estabelecimento=request.user).order_by('-data_criacao')
    return render(request, 'ofertas/minhas_ofertas.html', {'ofertas': ofertas})

@login_required
@estabelecimento_required
def editar_oferta(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk, estabelecimento=request.user)
    if request.method == 'POST':
        form = OfertaForm(request.POST, request.FILES, instance=oferta)
        if form.is_valid():
            form.save()
            messages.success(request, "Oferta atualizada com sucesso!")
            return redirect('ofertas:minhas_ofertas')
    else:
        form = OfertaForm(instance=oferta)
    return render(request, 'ofertas/editar_oferta.html', {'form': form, 'oferta': oferta})

@login_required
@estabelecimento_required
def excluir_oferta(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk, estabelecimento=request.user)
    if request.method == 'POST':
        oferta.delete()
        messages.success(request, "Oferta excluída com sucesso!")
        return redirect('ofertas:minhas_ofertas')
    return render(request, 'ofertas/excluir_oferta.html', {'oferta': oferta})

# ============================
# INSTITUIÇÃO VIEWS
# ============================

@login_required
@instituicao_required
def ofertas_disponiveis(request):
    query = request.GET.get('q')
    validade_produto = request.GET.get('validade_produto')

    ofertas = Oferta.objects.filter(disponivel=True, data_expiracao_oferta__gt=datetime.now())

    if query:
        ofertas = ofertas.filter(
            Q(nome_produto__icontains=query) |
            Q(descricao__icontains=query) |
            Q(estabelecimento__nome_fantasia__icontains=query)
        )
    if validade_produto:
        ofertas = ofertas.filter(data_validade_produto__gte=validade_produto)

    return render(request, 'ofertas/ofertas_disponiveis.html', {
        'ofertas': ofertas,
        'query': query,
        'validade_produto': validade_produto
    })

@login_required
@instituicao_required
def reservar_oferta(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk, disponivel=True, data_expiracao_oferta__gt=datetime.now())

    if request.method == 'POST':
        quantidade_reservar = int(request.POST.get('quantidade', 0))
        if quantidade_reservar > 0 and quantidade_reservar <= oferta.quantidade:
            reserva, created = Reserva.objects.get_or_create(
                oferta=oferta,
                instituicao=request.user,
                defaults={'quantidade_reservada': quantidade_reservar}
            )
            if not created:
                reserva.quantidade_reservada += quantidade_reservar
                reserva.save()

            oferta.quantidade -= quantidade_reservar
            if oferta.quantidade == 0:
                oferta.disponivel = False
            oferta.save()
            messages.success(request, f"Você reservou {quantidade_reservar} unidades de {oferta.nome_produto} com sucesso!")
            return redirect('ofertas:ofertas_disponiveis')
        else:
            messages.error(request, "Quantidade inválida ou superior à disponível.")

    return render(request, 'ofertas/reservar_oferta.html', {'oferta': oferta})

@login_required
@instituicao_required
def minhas_reservas(request):
    reservas = Reserva.objects.filter(instituicao=request.user).order_by('-data_reserva')
    return render(request, 'ofertas/minhas_reservas.html', {'reservas': reservas})
