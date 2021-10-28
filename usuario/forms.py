from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


from .models import User, Perfil_Usuario


# class MyCustomInput(InputMask):
#    mask = {'cpf': '000.000.000-00'}, {'cnpj': '00.000.000/0000-00'}


# USUÁRIO
class Cadastro_Usuario_Form(UserCreationForm):

    OPCAO_PESSOA = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica')
        )

    pessoa  = forms.ChoiceField(label='Pessoa', choices=OPCAO_PESSOA, widget=forms.RadioSelect)

    class Meta:
        model = get_user_model()
        fields = ['pessoa', 'email',]

    def save(self, user):
        user.pessoa = self.cleaned_data['pessoa']
        user.save()
   

class Editar_Usuario_Form(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ['email',]



# PERFIL
class Cadastro_Perfil_PF_Form(forms.ModelForm):
    nome       = forms.CharField(label='Nome Completo')
    cpf_cnpj   = forms.CharField(label='CPF')
    class Meta:
        model   = Perfil_Usuario
        fields  = ['nome', 'cpf_cnpj', 'celular', 'cep', 'endereco', 'numero', 'cidade', 'estado']


class Cadastro_Perfil_PJ_Form(forms.ModelForm):
    nome       = forms.CharField(label='Razão Social')
    cpf_cnpj   = forms.CharField(label='CNPJ')
    class Meta:
        model   = Perfil_Usuario
        fields  = ['nome', 'cpf_cnpj', 'celular', 'cep', 'endereco', 'numero', 'cidade', 'estado']


# SUPERUSUÁRIO
# Lista de usuários
@user_passes_test(lambda u: u.is_superuser)
def list_users(request):
    object = User.objects.all()
    context = {
        'object': object,
    }
    return render(request, 'account/list_users.html', context)


class Editar_Usuario_Admin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'equipe', 'ativo',]
    
    def save(self, request):
        user = super(Editar_Usuario_Admin, self).save(request)
        user.email = self.cleaned_data['email']
        return user

        


        