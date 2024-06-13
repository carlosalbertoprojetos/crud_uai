from django.urls import path
from django.views.generic.base import TemplateView


from . import views


app_name = 'usuario'


urlpatterns = [
    path('painel/', views.dashboard_View, name='dashboard'),
    path('<int:pk>/detalhes/', views.Detalhes_Usuario_View.as_view(), name='detalhes_usuario'),
    path('<int:pk>/editar/', views.Editar_Usuario_View.as_view(), name='editar_usuario'),

    # Acesso por usuários admin
    path('users/', views.listar_usuarios, name='listar_usuarios_admin'),
    path('<int:pk>/edituser/', views.Editar_Usuarios_AdminView.as_view() , name='editar_usuarios_admin'),

    # Perfis
    path('perfil/',views.Cadastro_Perfil_View.as_view(), name='cadastro_perfil'),
    path('aprovacao/', TemplateView.as_view(template_name='account/profile_message.html'), name='approval'),

    path('detalhes/perfil/<int:user_id>/', views.detalhes_perfil_user, name='detalhes_perfil'),

    path('editar/perfil/<int:user_id>/', views.editar_perfil, name='editar_perfil'),
    path('salvar/perfil/<int:user_id>/', views.salvar_perfil, name='salvar_perfil'),
]





