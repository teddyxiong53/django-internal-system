from django.shortcuts import render, get_object_or_404
from .models import Employee


def hr_dashboard(request):
    return render(request, 'hr_app/hr_dashboard.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'hr_app/employee_list.html', {'employees': employees})


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hr_app/employee_detail.html', {'employee': employee})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'hr_app/employee_form.html', {'form': form})


def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'hr_app/employee_form.html', {'form': form, 'employee': employee})


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'hr_app/employee_confirm_delete.html', {'employee': employee})
