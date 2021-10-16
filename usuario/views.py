from django.shortcuts import render
from django.contrib.auth.models import User



# redirecionar login para dahsboard do usuário
def dashboard_View(request):
    object = User.objects.filter(id=request.user.id)
    context = {
        'object': object,
    }
    
    return render(request, 'dashboard.html', context)


