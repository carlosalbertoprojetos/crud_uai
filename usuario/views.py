from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


from .models import User, Perfil_Usuario
from .forms import Editar_Usuario_Form, Cadastro_Perfil_PF_Form, Cadastro_Perfil_PJ_Form



# USUÁRIO
# Redirecionar login para dahsboard do usuário
def dashboard_View(request):
    object = User.objects.filter(id=request.user.id)
    template_name = 'account/dashboard.html'
    context = {
        'object': object,
    }
    return render(request, template_name, context)


class Detalhes_Usuario_View(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'usuario/detalhes_perfil.html'


# Listar usuários
@user_passes_test(lambda u: u.is_superuser) # somente para superusuários
def listar_usuarios(request):
    object = User.objects.all()
    context = {
        'object': object,
    }
    return render(request, 'usuario/lista_usuarios.html', context)



# Editar dados de qualquer usuário - somente para superusuários
class Editar_Usuarios_AdminView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'usuario/editar_usuario.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario:listar_usuarios_admin')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form)


class Editar_Usuario_View(LoginRequiredMixin, UpdateView):
    model = User
    form_class = Editar_Usuario_Form
    template_name = 'usuario/editar_usuario.html'
    success_url = reverse_lazy('usuario:dashboard')



# PERFIL
class Cadastro_Perfil_View(LoginRequiredMixin, CreateView):
    template_name = 'usuario/cadastro_perfil.html'
    form_class = Cadastro_Perfil_PF_Form
    success_url = reverse_lazy('usuario:approval')

    # seleciona o formulário a ser preenchido, conforme pessoa (física/jurídica)
    def get_form_class(self):
        pessoa = User.objects.get(id=self.request.user.id)
        if pessoa.pessoa == 'PJ':
            return Cadastro_Perfil_PJ_Form
        else:
            return Cadastro_Perfil_PF_Form

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()

        # torna a conta do usuário inativa para ser avaliada (aprovada/recusada)
        disable_user = User.objects.get(id=self.request.user.id)
        disable_user.ativo = False
        disable_user.save()
        return super().form_valid(form)




def detalhes_perfil_user(request, user_id):
    object = Perfil_Usuario.objects.get(user_id=user_id)
    return render(request, 'usuario/detalhes_perfil.html', {'object': object})


def editar_perfil(request, user_id):
    form = Perfil_Usuario.objects.get(user_id=user_id)
    context = {
        'form': form,
    }
    return render(request, 'usuario/editar_perfil.html', context)


def salvar_perfil(request, user_id):
    form = Perfil_Usuario.objects.get(user_id=user_id)
    nome            = request.POST.get('nome')
    cpf_cnpj        = request.POST.get('cpf_cnpj')
    celular         = request.POST.get('celular')
    cep             = request.POST.get('cep')
    endereco        = request.POST.get('endereco') 
    numero          = request.POST.get('numero')
    cidade          = request.POST.get('cidade')   
    estado          = request.POST.get('estado')
    form.user_id    = user_id
    form.nome       = nome
    form.cpf_cnpj   = cpf_cnpj
    form.celular    = celular
    form.cep        = cep
    form.endereco   = endereco
    form.numero     = numero
    form.cidade     = cidade
    form.estado     = estado
    form.save()
    return redirect('usuario:detalhes_perfil', user_id)





