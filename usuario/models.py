from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_active=True, is_staff=False):
        if not email:
            raise ValueError('O usuário precisa ter um email válido.')
        if not password:
            raise ValueError('Precisa inserir a senha correta.')

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.username = username
        user_obj.ativo = is_active
        user_obj.equipe = is_staff
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password=password,
            is_staff=True
        )
        return user



class User(AbstractBaseUser, PermissionsMixin):

    PROFILE_SITUACAO = {
        ('0', 'Pendente'),
        ('1', 'Aprovado'),
        ('2', 'Reprovado'),
    }

    email       = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    
    username    = models.CharField('Nome/Razão Social', max_length=255, unique=True)
    cpf_cnpj    = models.CharField('CPF/CNPJ', max_length=14, unique=True, null=True, blank=True)
    celular     = models.IntegerField('Celular', null=True)
    cep         = models.CharField('Cep', max_length=8)
    endereco    = models.CharField('Endereco', max_length=255)
    numero      = models.CharField('Número', max_length=8)
    cidade      = models.CharField('Cidade', max_length=255)
    estado      = models.CharField('Estado', max_length=255)    
    
    situacao    = models.CharField('Situação', max_length=13, choices=PROFILE_SITUACAO, default='Pendente')
    equipe      = models.BooleanField('Membro da equipe', default=False)
    ativo       = models.BooleanField('Usuário ativo', default=True)

    criadoem     = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado em'))
    atualizadoem = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado em'))

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']


    objects = UserManager()


    def get_full_name(self):
        return self.username or self.email

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "O usuário tem a permissão específica?"
        return True

    def has_module_perms(self, app_label):
        "O usuário tem permissões para visualizar o aplicativo?"
        return True


    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        elif username is int(username):
            # len(username) == 11
            kwargs = {'cpf': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None


    @property
    def is_active(self):
        "A conta está ativa?"
        return self.ativo
    
    @property
    def is_staff(self):
        "O usuário é um membro da equipe?"
        return self.equipe


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

        