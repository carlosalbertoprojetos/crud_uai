from django.urls import path

from . import views


app_name = 'usuario'


urlpatterns = [
    path('painel/', views.dashboard_View, name='dashboard'),
    path('<int:pk>/detalhes/', views.Detalhes_Usuario_View.as_view(), name='destalhes_usuario'),
    path('<int:pk>/editar/', views.Editar_Usuario_View.as_view(), name='editar_usuario'),

    # ACESSO ADMIN
    path('users/', views.listar_usuarios, name='listar_usuarios_admin'),
    path('<int:pk>/edituser/', views.Editar_Usuarios_AdminView.as_view() , name='editar_usuarios_admin'),
]


