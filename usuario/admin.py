from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# from .forms import Perfil_Form
from .models import Perfil_Usuario


class Perfil_Usuario_Admin(admin.StackedInline):
    model = Perfil_Usuario
    fieldsets = (
        ('Permissões', {'fields': ('situacao',)}),
        ('Usuário', {'fields': (('nome', 'cpf_cnpj'),)}),
        ('Contato', {'fields': ('celular',)}),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': ('cep', ('endereco', 'numero'), ('cidade', 'estado'),
            )}),
    )

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Usuário', {'fields': ('email', 'pessoa',)}),
        ('Permissões', {
            'classes': ('collapse',),
            'fields': ('ativo', 'groups', 'user_permissions'),}),
        ('Registros', {
            'classes': ('collapse',),
            'fields': ('last_login', 'data_registro')
            }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'pessoa', 'ativo', 'equipe', 'admin')
    list_filter = ('pessoa', 'ativo', 'equipe',)
    search_fields = ('email',)
    ordering = ('email',)
    inlines = [
        Perfil_Usuario_Admin,
    ]

admin.site.register(get_user_model(), UserAdmin)


