from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AppPermission

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 为新用户创建默认权限
            AppPermission.objects.create(user=user, app_name='portal', can_access=True)
            AppPermission.objects.create(user=user, app_name='oa_app', can_access=True)
            username = form.cleaned_data.get('username')
            messages.success(request, f'账号 {username} 创建成功!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'portal/register.html', {'form': form})

@login_required
def dashboard(request):
    # 获取用户可访问的应用列表
    user_permissions = AppPermission.objects.filter(user=request.user, can_access=True)
    apps = [
        {
            'name': perm.get_app_name_display(),
            'url': f'/{perm.app_name}/',
            'description': f'访问{perm.get_app_name_display()}应用'
        }
        for perm in user_permissions
    ]
    return render(request, 'portal/dashboard.html', {'apps': apps})
