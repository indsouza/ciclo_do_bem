from django.contrib import admin
from .models import Oferta, Reserva

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'estabelecimento', 'data_validade_produto', 'data_expiracao_oferta', 'quantidade', 'disponivel')
    list_filter = ('disponivel', 'estabelecimento', 'data_validade_produto')
    search_fields = ('nome_produto', 'estabelecimento__nome_fantasia')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('oferta', 'instituicao', 'quantidade_reservada', 'data_reserva', 'confirmada')
    list_filter = ('confirmada', 'instituicao')
    search_fields = ('oferta__nome_produto', 'instituicao__nome_fantasia')

admin.site.register(Oferta, OfertaAdmin)
admin.site.register(Reserva, ReservaAdmin)
