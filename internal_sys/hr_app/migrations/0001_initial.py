# Generated by Django 5.2.1 on 2025-05-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('position', models.CharField(max_length=100, verbose_name='职位')),
                ('department', models.CharField(max_length=100, verbose_name='部门')),
                ('hire_date', models.DateField(verbose_name='入职日期')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='薪资')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=20, verbose_name='联系电话')),
            ],
            options={
                'verbose_name': '员工信息',
                'verbose_name_plural': '员工信息',
            },
        ),
    ]
