from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
        labels = {
            'name': '客户名称',
            'phone': '联系电话',
            'email': '电子邮箱',
            'address': '联系地址'
        }