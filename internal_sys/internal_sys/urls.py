from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from portal import views as portal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portal_views.dashboard, name='dashboard'),
    path('register/', portal_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('oa_app/', include('oa_app.urls')),
    path('hr_app/', include('hr_app.urls')),
]
