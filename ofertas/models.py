from django.db import models
from estabelecimentos.models import Estabelecimento
from instituicoes.models import Instituicao

class Oferta(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, related_name='ofertas')
    nome_produto = models.CharField(max_length=200)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='ofertas_fotos/', blank=True, null=True)
    data_validade_produto = models.DateField()
    data_expiracao_oferta = models.DateTimeField()
    quantidade = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome_produto} de {self.estabelecimento.nome_fantasia}'

class Reserva(models.Model):
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name='reservas')
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='minhas_reservas')
    quantidade_reservada = models.PositiveIntegerField()
    data_reserva = models.DateTimeField(auto_now_add=True)
    confirmada = models.BooleanField(default=False) # Se o estabelecimento confirmou a reserva

    class Meta:
        unique_together = ('oferta', 'instituicao') # Uma instituição só pode reservar uma oferta uma vez

    def __str__(self):
        return f'Reserva de {self.quantidade_reservada} de {self.oferta.nome_produto} por {self.instituicao.nome_fantasia}'

