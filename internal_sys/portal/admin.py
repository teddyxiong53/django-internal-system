from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import AppPermission

class AppPermissionInline(admin.TabularInline):
    model = AppPermission
    extra = 1

class CustomUserAdmin(UserAdmin):
    inlines = [AppPermissionInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')

# 重新注册User模型
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(AppPermission)
class AppPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'app_name', 'can_access')
    list_filter = ('app_name', 'can_access')
    search_fields = ('user__username', 'app_name')
