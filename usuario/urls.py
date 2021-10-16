
from django.urls import path


from . import views

app_name = 'usuario'


urlpatterns = [
    path('', views.dashboard_View, name='dashboard'),
]
