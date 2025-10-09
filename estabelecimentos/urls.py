from django.urls import path
from . import views  # importa as views criadas
from django.views.generic import TemplateView

urlpatterns = [
    # Rota que processa o cadastro de verdade (salva no banco)
    path('cadastrar_estabelecimento/', views.cadastrar_estabelecimento, name='cadastrar_estabelecimento'),

    # Página de login (pode ser estática por enquanto)
    path('login_estabelecimento/', TemplateView.as_view(template_name='login_estabelecimento.html'), name='login_estabelecimento'),
]
