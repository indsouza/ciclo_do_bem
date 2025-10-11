from django.urls import path
from . import views

app_name = 'estabelecimentos'  # Necessário para usar o namespace

urlpatterns = [
    path('cadastrar/', views.cadastrar_estabelecimento, name='cadastrar_estabelecimento'),
    path('login/', views.login_estabelecimento, name='login_estabelecimento'),
    path('perfil/', views.perfil_estabelecimento, name='perfil_estabelecimento'),
    path('logout/', views.logout_estabelecimento, name='logout_estabelecimento'),
]
