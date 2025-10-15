from django.contrib.auth.backends import BaseBackend
from .models import Estabelecimento

class EstabelecimentoBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            estabelecimento = Estabelecimento.objects.get(email=email)
            if estabelecimento.check_password(password):
                return estabelecimento
        except Estabelecimento.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Estabelecimento.objects.get(pk=user_id)
        except Estabelecimento.DoesNotExist:
            return None

