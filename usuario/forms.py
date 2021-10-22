from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


from .models import User, Perfil_Usuario


# class MyCustomInput(InputMask):
#    mask = {'cpf': '000.000.000-00'}, {'cnpj': '00.000.000/0000-00'}

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
   

    # def clean_email(self): # confere se o email informado já está cadastrado
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("Este email já está sendo utilizado")
    #     return email

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     password_2 = cleaned_data.get("password_2")
    #     if password is not None and password != password_2:
    #         self.add_error("password_2", "As senhas precisam ser iguais.")
    #     return cleaned_data


# class Criar_Usuario_Admin(forms.ModelForm):

#     # REGIME_JURIDICO = {
#     #     ('PF', 'Física'),
#     #     ('PJ', 'Jurídica'),
#     # }

#     # pessoa = forms.ChoiceField(choices=REGIME_JURIDICO)
#     # password = forms.CharField(widget=forms.PasswordInput)
#     # password_2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['pessoa', 'email', 'equipe', 'ativo', 'superusuario',]

#     # def clean(self):
#     #     cleaned_data = super().clean()
#     #     password = cleaned_data.get("password")
#     #     password_2 = cleaned_data.get("password_2")
#     #     if password is not None and password != password_2:
#     #         self.add_error("password_2", "As senhas precisam ser iguais.")
#     #     return cleaned_data

#     # def save(self, commit=True):
#     #     # Save the provided password in hashed format
#     #     user = super().save(commit=False)
#     #     user.pessoa = self.cleaned_data["pessoa"]
#     #     user.set_password(self.cleaned_data["password"])
#     #     if commit:
#     #         user.save()
#     #     return user


class Editar_Usuario_Admin(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'equipe', 'ativo',]
    
    def save(self, request):
        
        user = super(Editar_Usuario_Admin, self).save(request)
        user.email = self.cleaned_data['email']
        return user


class Editar_Usuario_Form(forms.ModelForm):

    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email',)


    # def clean_password(self):
    #     return self.initial["password"]



# class PF_Register_Form(forms.ModelForm):
# class Register_Form(forms.ModelForm):
#     class Meta:
#         model = User
#         # fields = ['email', 'username', 'cpf_cnpj', 'celular', 'endereco', ]
#         fields = '__all__'


# class PJ_Register_Form(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'cpf_cnpj', 'celular', 'endereco', ]


class Perfil_Form(forms.ModelForm):

    class Meta:
        model = Perfil_Usuario
        fields = ['nome', 'cpf_cnpj', 'celular', 'cep', 'endereco', 'numero', 'cidade', 'estado', 'situacao']
        

