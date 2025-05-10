from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer
from .forms import CustomerForm

class CustomerListView(ListView):
    model = Customer
    template_name = 'crm_app/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 10

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'crm_app/customer_form.html'
    success_url = reverse_lazy('crm:customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'crm_app/customer_form.html'
    success_url = reverse_lazy('crm:customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'crm_app/customer_confirm_delete.html'
    success_url = reverse_lazy('crm:customer_list')
