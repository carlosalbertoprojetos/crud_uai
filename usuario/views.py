from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
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
    success_url = reverse_lazy('usuario:lista_usuarios')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form)


class Detalhes_Usuario_View(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'usuario/detalhes_usuario.html'


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

    # def direct_success_url(self):
    #     user_pessoa = User.objects.filter(id=self.request.user.id)
    #     if user_pessoa.pessoa == 'PF':
    #         form_class = Cadastro_Perfil_PF_Form
    #     else:
    #         form_class = Cadastro_Perfil_PJ_Form
    #     return form_class

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()

        disable_user = User.objects.get(id=self.request.user.id)
        disable_user.is_active = False
        disable_user.save()
            
        return super().form_valid(form)


class Detalhes_Perfil_View(LoginRequiredMixin, DetailView):
    model = Perfil_Usuario
    template_name = 'detalhes_perfil.html'


class Editar_Perfil_View(LoginRequiredMixin, UpdateView):
    template_name = 'editar_perfil.html'
    success_url = reverse_lazy('profile:list_user_profile')
    
    def direct_success_url(self):
        user_pessoa = User.objects.filter(id=self.request.user.id)
        if user_pessoa.pessoa == 'PF':
            form_class = Cadastro_Perfil_PF_Form
        else:
            form_class = Cadastro_Perfil_PJ_Form
        return form_class

    
