from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy



from .models import User
from .forms import Editar_Usuario_Form



# redirecionar login para dahsboard do usuário
def dashboard_View(request):
    object = User.objects.filter(id=request.user.id)
    template_name = 'account/dashboard.html'
    context = {
        'object': object,
    }
    
    return render(request, template_name, context)



# usuario
@user_passes_test(lambda u: u.is_superuser) # somente para superusuários
def listar_usuarios(request):
    object = User.objects.all()
    context = {
        'object': object,
    }
    return render(request, 'usuario/lista_usuarios.html', context)


# editar dados de qualquer usuário - somente para superusuários
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



