from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SignupForm, Editar_Usuario_Form, Perfil_Form
from .models import User, Perfil_Usuario



class Usuario_Admin(UserAdmin):
    add_form = SignupForm
    form = Editar_Usuario_Form
    model = User
    list_display = ('email', 'equipe', 'ativo', 'superusuario',)
    list_filter = ('equipe', 'ativo',)
    fieldsets = (
        ('Usuário', {'fields': ('email', 'pessoa')}),
        ('Permissões', {'fields': ('ativo', 'equipe',  'superusuario',)}),
    )
    search_fields = ('pessoa', 'email',)
    ordering = ('-criadoem', )


admin.site.register(User, Usuario_Admin)


class Perfil_usuario(admin.ModelAdmin):
    model = Perfil_Usuario
    add_form = Perfil_Form
    list_display = ('nome', 'cpf_cnpj', 'celular', 'user','situacao',)
    list_filter = ('nome', 'cpf_cnpj', 'user',)
    fieldsets = (
        ('Usuário', {'fields': ('nome', 'user')}),
        ('Documento', {'fields': ('cpf_cnpj',)}),
        ('Contato', {'fields': ('celular',)}),
        ('Endereço', {'fields': ('cep', 'endereco', 'numero', 'cidade', 'estado',)}),
        ('Permissões', {'fields': ('situacao', )}),
    )
    search_fields = ('nome', 'email', 'cpf_cnpj',)
    ordering = ('-criadoem', )



