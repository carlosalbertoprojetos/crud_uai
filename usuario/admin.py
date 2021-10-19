from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import Criar_Usuario_Admin, Editar_Usuario_Admin, Perfil_Form
from .models import User, Perfil_Usuario



class Usuario_Admin(BaseUserAdmin):
    add_form = Criar_Usuario_Admin
    # form = Editar_Usuario_Admin

    list_display = ('email', 'pessoa', 'ativo', 'equipe', 'superusuario',)
    list_filter = ('equipe', 'ativo', 'email',)
    fieldsets = (
        ('Usuário', {'fields': ('email', 'pessoa', )}),
        ('Permissões', {'fields': ('ativo', 'equipe', 'superusuario',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('pessoa', 'email', 'password',)}
        ),
    )
    search_fields = ('pessoa', 'email', 'ativo', 'equipe',)
    ordering = ('-criadoem', )

admin.site.register(User, Usuario_Admin)


class Perfil_Usuario_Admin(admin.ModelAdmin):
    model = Perfil_Usuario
    add_form = Perfil_Form
    list_display = ('nome', 'user', 'cpf_cnpj', 'celular', 'situacao',)
    list_filter = ('nome', 'cpf_cnpj', )
    fieldsets = (
        ('Usuário', {'fields': ('nome', 'user', )}),
        ('Documento', {'fields': ('cpf_cnpj',)}),
        ('Contato', {'fields': ('celular',)}),
        ('Endereço', {'fields': ('cep', 'endereco', 'numero', 'cidade', 'estado',)}),
        ('Permissões', {'fields': ('situacao', )}),
    )
    search_fields = ('nome', 'email', 'cpf_cnpj',)
    ordering = ('-nome', )


admin.site.register(Perfil_Usuario, Perfil_Usuario_Admin)


