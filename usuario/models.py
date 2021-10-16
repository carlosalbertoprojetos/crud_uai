from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    def create_user(self, email, nome, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('O usuário precisa ter um email válido.')
        if not password:
            raise ValueError('Precisa inserir a senha correta.')

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.nome = nome
        user_obj.ativo = is_active
        user_obj.equipe = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, nome, password=None):
        user = self.create_user(
            email,
            nome,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, nome, password=None):
        user = self.create_user(
            email,
            nome,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user



class User(AbstractBaseUser, PermissionsMixin):

    PROFILE_SITUACAO = {
        ('0', 'Pendente'),
        ('1', 'Aprovado'),
        ('2', 'Reprovado'),
    }

    email       = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    nome        = models.CharField('Nome', max_length=255, unique=True)
    cpf        = models.CharField('Nome', max_length=11, unique=True)
    razao_social= models.CharField('Razão Social', max_length=255, unique=True)
    cnpj        = models.CharField('Nome', max_length=14, unique=True)
    celular     = models.IntegerField('Celular', null=True)
    endereco    = models.CharField('Endereco', max_length=255)
    situacao    = models.CharField('Situação', max_length=13, choices=PROFILE_SITUACAO, default='Pendente')
    equipe      = models.BooleanField('Membro da equipe', default=False)
    ativo       = models.BooleanField('Usuário ativo', default=True)
    admin       = models.BooleanField('Usuário admin', default=False)

    criadoem     = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado em'))
    atualizadoem = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado em'))

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['nome']


    def get_full_name(self):
        return self.nome or self.email

    def __str__(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        "O usuário tem a permissão específica?"
        return True

    def has_module_perms(self, app_label):
        "O usuário tem permissões para visualizar o aplicativo?"
        return True

    @property
    def is_active(self):
        "A conta está ativa?"
        return self.ativo
    
    @property
    def is_staff(self):
        "O usuário é um membro da equipe?"
        return self.equipe

    @property
    def is_admin(self):
        "O usuário é membro Admin?"
        return self.admin

    objects = UserManager()

