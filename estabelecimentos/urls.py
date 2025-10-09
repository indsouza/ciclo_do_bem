from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('cadastrar_estabelecimento/', TemplateView.as_view(template_name='cadastrar_estabelecimento.html'), name='cadastrar_estabelecimento'),
    path('login_estabelecimento/', TemplateView.as_view(template_name='login_estabelecimento.html'), name='login_estabelecimento'),
]

