from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import Cadastro_Usuario_Form, Editar_Usuario_Form
from .models import User



class Custom_User_Admin(UserAdmin):
    add_form = Cadastro_Usuario_Form
    form = Editar_Usuario_Form
    model = User
    list_display = ('email', 'username', 'cpf_cnpj', 'equipe', 'situacao', 'ativo',)
    list_filter = ('username', 'cpf_cnpj', 'equipe', 'ativo',)
    fieldsets = (
        (None, {'fields': ('username', 'email',)}),
        ('Documento', {'fields': ('cpf_cnpj',)}),
        ('Contato', {'fields': ('celular',)}),
        ('Endereço', {'fields': ('endereco',)}),
        ('Permissões', {'fields': ('situacao', 'equipe', 'ativo')}),
    )
    search_fields = ('username', 'email', 'cpf_cnpj',)
    ordering = ('-criadoem', )


admin.site.register(User, Custom_User_Admin)


