from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'estabelecimentos'

urlpatterns = [
    path('cadastrar_estabelecimento/', views.cadastrar_estabelecimento, name='cadastrar_estabelecimento'),
    path('login_estabelecimento/', TemplateView.as_view(template_name='login_estabelecimento.html'), name='login_estabelecimento'),
]
