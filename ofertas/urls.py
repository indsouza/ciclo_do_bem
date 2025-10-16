from django.urls import path
from . import views

app_name = 'ofertas'

urlpatterns = [
    # Estabelecimento
    path("criar_oferta/", views.criar_oferta, name="criar_oferta"),
    path("minhas_ofertas/", views.minhas_ofertas, name="minhas_ofertas"),
    path("editar_oferta/<int:pk>/", views.editar_oferta, name="editar_oferta"),
    path("excluir_oferta/<int:pk>/", views.excluir_oferta, name="excluir_oferta"),

    # Instituição
    path("disponiveis/", views.ofertas_disponiveis, name="ofertas_disponiveis"),
    path("reservar/<int:pk>/", views.reservar_oferta, name="reservar_oferta"),
    path("minhas_reservas_instituicao/", views.minhas_reservas, name="minhas_reservas_instituicao"),
]
