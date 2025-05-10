from django.db import models

class Customer(models.Model):
    name = models.CharField('客户名称', max_length=100)
    phone = models.CharField('联系电话', max_length=20)
    email = models.EmailField('电子邮箱')
    address = models.TextField('联系地址')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后更新', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = '客户信息管理'
