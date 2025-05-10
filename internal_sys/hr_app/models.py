from django.db import models

class Employee(models.Model):
    name = models.CharField('姓名', max_length=100)
    position = models.CharField('职位', max_length=100)
    department = models.CharField('部门', max_length=100)
    hire_date = models.DateField('入职日期')
    salary = models.DecimalField('薪资', max_digits=10, decimal_places=2)
    email = models.EmailField('邮箱', unique=True)
    phone = models.CharField('联系电话', max_length=20)

    def __str__(self):
        return f'{self.name} - {self.position}'

    class Meta:
        verbose_name = '员工信息'
        verbose_name_plural = '员工信息'
