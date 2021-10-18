from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

User = get_user_model()



# class MyCustomInput(InputMask):
#    mask = {'cpf': '000.000.000-00'}, {'cnpj': '00.000.000/0000-00'}

class Cadastro_Usuario_Form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'cpf_cnpj', 'celular', 'endereco', 'situacao', 'equipe', 'ativo',]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "As senhas precisam ser iguais.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class Editar_Usuario_Form(forms.ModelForm):

    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'username', 'cpf_cnpj', 'celular', 'endereco',]

    # def clean_password(self):
    #     return self.initial["password"]



# class PF_Register_Form(forms.ModelForm):
class Register_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'cpf_cnpj', 'celular', 'endereco', ]


# class PJ_Register_Form(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'cpf_cnpj', 'celular', 'endereco', ]


