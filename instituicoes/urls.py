from django.urls import path
from . import views

app_name = 'instituicoes'  # 🔹 define o namespace do app

urlpatterns = [
    path('cadastrar/', views.cadastrar_instituicao, name='cadastrar_instituicao'),
    path('login/', views.login_instituicao, name='login_instituicao'),
    path('logout/', views.logout_instituicao, name='logout_instituicao'),
    path('perfil/', views.perfil_instituicao, name='perfil_instituicao'),
]
