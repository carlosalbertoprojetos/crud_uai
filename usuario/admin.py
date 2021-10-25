from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# from .forms import Perfil_Form
from .models import Perfil_Usuario


class Perfil_Usuario_Admin(admin.StackedInline):
    model = Perfil_Usuario
    # add_form = Perfil_Form
    # list_display = ('nome', 'user', 'cpf_cnpj', 'celular', 'situacao',)
    # list_filter = ('nome', 'cpf_cnpj', )
    fieldsets = (
        ('Permissões', {'fields': ('situacao',)}),
        ('Usuário', {'fields': (('nome', 'cpf_cnpj'),)}),
        ('Contato', {'fields': ('celular',)}),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': ('cep', ('endereco', 'numero'), ('cidade', 'estado'),
            )}),
    )
    # search_fields = ('nome', 'email', 'cpf_cnpj',)
    # ordering = ('-nome', )


# admin.site.register(Perfil_Usuario, Perfil_Usuario_Admin)


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




# class Perfil_Usuario_Admin(admin.ModelAdmin):
#     model = Perfil_Usuario
#     add_form = Perfil_Form
#     list_display = ('nome', 'user', 'cpf_cnpj', 'celular', 'situacao',)
#     list_filter = ('nome', 'cpf_cnpj', )
#     fieldsets = (
#         ('Usuário', {'fields': ('nome', 'user', )}),
#         ('Documento', {'fields': ('cpf_cnpj',)}),
#         ('Contato', {'fields': ('celular',)}),
#         ('Endereço', {'fields': ('cep', 'endereco', 'numero', 'cidade', 'estado',)}),
#         ('Permissões', {'fields': ('situacao', )}),
#     )
#     search_fields = ('nome', 'email', 'cpf_cnpj',)
#     ordering = ('-nome', )


# admin.site.register(Perfil_Usuario, Perfil_Usuario_Admin)


