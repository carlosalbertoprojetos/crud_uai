from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext as _

from datetime import datetime


class UserManager(BaseUserManager):
    
    def create_user(self, pessoa, email, password=None, is_active=True, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError('O usuário precisa ter um email válido.')
        if not password:
            raise ValueError('Precisa inserir a senha correta.')
        
        user = self.model(email=self.normalize_email(email)
        )
        user.pessoa = pessoa
        user.set_password(password)
        user.ativo = is_active
        user.equipe = is_staff
        user.admin = is_superuser
        user.save(using=self._db)

        return user
        

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            pessoa='PF',
            is_staff=True,
            is_superuser=True
        )

        return user



class User(AbstractBaseUser, PermissionsMixin):

    # username    = None
    email       = models.EmailField('Email', unique=True) 
    pessoa      = models.CharField('Pessoa', max_length=2)

    ativo       = models.BooleanField(default=True)
    equipe      = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)

    data_registro = models.DateTimeField('Data do registro', default=datetime.now)
    
    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email


    @property
    def is_active(self):
        "A conta está ativa?"
        return self.ativo

    @property
    def is_staff(self):
        "O usuário é membro da equipe?"
        return self.equipe

    @property
    def is_superuser(self):
        "O usuário é Admin?"
        return self.admin


    objects = UserManager()


    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"



class Perfil_Usuario(models.Model):       

    PROFILE_SITUACAO = {
            ('0', 'Pendente'),
            ('1', 'Aprovado'),
            ('2', 'Reprovado'),
    }

    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    nome        = models.CharField('Nome/Razão Social', max_length=255, unique=True)
    cpf_cnpj    = models.CharField('CPF/CNPJ', max_length=17, unique=True)
    celular     = models.IntegerField('Celular', null=True)
    
    cep         = models.CharField('Cep', max_length=8)
    endereco    = models.CharField('Endereco', max_length=255)
    numero      = models.CharField('Número', max_length=8)
    cidade      = models.CharField('Cidade', max_length=255)
    estado      = models.CharField('Estado', max_length=255)    
    
    situacao    = models.CharField('Situação', max_length=13, choices=PROFILE_SITUACAO, default='Pendente')

    atualizadoem = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado em'))

    def __str__(self):
        return self.user.email or self.nome or self.cpf_cnpj

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'




