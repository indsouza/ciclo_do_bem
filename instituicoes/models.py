from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

HORARIOS = [(f"{h:02}:00", f"{h:02}:00") for h in range(6, 23)]

class InstituicaoManager(BaseUserManager):
    def create_user(self, email, senha=None, **extra_fields):
        if not email:
            raise ValueError("O campo email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if senha:
            user.set_password(senha)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, senha=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, senha, **extra_fields)

class Instituicao(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    razao_social = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18)
    nome_fantasia = models.CharField(max_length=150)
    inscricao_estadual = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=20)
    horario_inicio = models.CharField(max_length=5, choices=HORARIOS)
    horario_fim = models.CharField(max_length=5, choices=HORARIOS)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    nome_responsavel = models.CharField(max_length=150)
    cargo_funcao = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    telefone_responsavel = models.CharField(max_length=20)
    responsavel_tecnico = models.CharField(max_length=150, blank=True, null=True)
    formacao_academica = models.CharField(max_length=150, blank=True, null=True)
    conselho_classe = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='instituicoes_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='instituicoes_user_permissions', blank=True)

    objects = InstituicaoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['razao_social', 'cnpj']

    def __str__(self):
        return self.nome_fantasia
