from django.contrib.auth.backends import BaseBackend
from .models import Instituicao

class InstituicaoBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Instituicao.objects.get(email=email)
            if user.check_password(password):
                return user
        except Instituicao.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Instituicao.objects.get(pk=user_id)
        except Instituicao.DoesNotExist:
            return None
