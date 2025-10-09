from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('criar_oferta/', TemplateView.as_view(template_name='criar_oferta.html'), name='criar_oferta'),
    path('editar_oferta/', TemplateView.as_view(template_name='editar_oferta.html'), name='editar_oferta'),
    path('excluir_oferta/', TemplateView.as_view(template_name='excluir_oferta.html'), name='excluir_oferta'),
    path('minhas_ofertas/', TemplateView.as_view(template_name='minhas_ofertas.html'), name='minhas_ofertas'),
]