from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, Perfil_Usuario

User = get_user_model()


# class MyCustomInput(InputMask):
#    mask = {'cpf': '000.000.000-00'}, {'cnpj': '00.000.000/0000-00'}

class SignupForm(forms.ModelForm):

    REGIME_JURIDICO = {
        ('0', 'Física'),
        ('1', 'Jurídica'),
    }
   
    pessoa = forms.ChoiceField(choices=REGIME_JURIDICO)

    class Meta:
        model = User
        fields = ['pessoa','email',]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     password_2 = cleaned_data.get("password_2")
    #     if password is not None and password != password_2:
    #         self.add_error("password_2", "As senhas precisam ser iguais.")
    #     return cleaned_data

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user


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
        

