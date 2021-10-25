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

        disable_user = User.objects.get(id=self.request.user.id)
        disable_user.ativo = False
        disable_user.save()
           
        return super().form_valid(form)


class Detalhes_Perfil_View(LoginRequiredMixin, DetailView):
    model = Perfil_Usuario
    template_name = 'usuario/detalhes_perfil.html'




# class Editar_Perfil_View(LoginRequiredMixin, UpdateView):
#     template_name = 'usuario/editar_perfil.html'
    # form_class = Cadastro_Perfil_PF_Form
    # success_url = reverse_lazy('usuario:dashboard')
    
    # def get_form_class(self):
    #     if self.user.pessoa ==  'PJ':
    #         form_class=Cadastro_Perfil_PJ_Form
    #     return form_class

    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.user = self.request.user
    #     obj.save()  


class Editar_Perfil_View(UpdateView):
    model = Perfil_Usuario
    fields = '__all__'
    template_name = 'usuario/editar_perfil.html'
    success_url = reverse_lazy('usuario:dashboard')

