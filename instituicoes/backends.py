from django.contrib.auth.backends import BaseBackend
from .models import Instituicao

class InstituicaoBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            instituicao = Instituicao.objects.get(email=email)
            # Para Instituicao, a senha não é hashed, então comparamos diretamente
            if instituicao.check_password(password):
                return instituicao
        except Instituicao.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Instituicao.objects.get(pk=user_id)
        except Instituicao.DoesNotExist:
            return None

