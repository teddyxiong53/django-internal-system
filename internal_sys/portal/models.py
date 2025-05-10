from django.db import models
from django.contrib.auth.models import User

class AppPermission(models.Model):
    APP_CHOICES = [
        ('portal', 'Portal'),
        ('hr_app', 'HR Application'),
        ('crm_app', 'CRM Application'),
        ('oa_app', 'OA Application'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='app_permissions')
    app_name = models.CharField(max_length=50, choices=APP_CHOICES)
    can_access = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'app_name']
        verbose_name = '应用权限'
        verbose_name_plural = '应用权限'

    def __str__(self):
        return f'{self.user.username} - {self.get_app_name_display()} - {"可访问" if self.can_access else "禁止访问"}'
