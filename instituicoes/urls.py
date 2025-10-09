from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('cadastrar_instituicao/', TemplateView.as_view(template_name='cadastrar_instituicao.html'), name='cadastrar_instituicao'),
    path('login_instituicao/', TemplateView.as_view(template_name='login_instituicao.html'), name='login_instituicao'),
]