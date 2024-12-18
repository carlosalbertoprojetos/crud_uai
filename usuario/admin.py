from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class Custom_User_Admin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'nome', 'cpf', 'razao_social', 'cnpj', 'situacao', 'ativo',)
    list_filter = ('nome', 'razao_social', 'cpf', 'cnpj', 'equipe', 'ativo',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('situacao', 'equipe', 'ativo')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'equipe', 'ativo')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, Custom_User_Admin)


