from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from portal import views as portal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portal_views.dashboard, name='dashboard'),
    path('register/', portal_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
