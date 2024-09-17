from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages

from employee.forms import EmployeeForm

from .models import Employee

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

    else:
        form = AuthenticationForm()
    context = {
        "form": form
        }
    return render(request, "account/login.html", context)


def logout_view(request):
    if request.user.is_authenticated:  
        logout(request) 
    return redirect("login_view")


@login_required
def home(request):
    employees = Employee.objects.all()
    employee = None
    if not request.user.is_superuser:
        print(request.user.username)
        print(request.user)
        employee = get_object_or_404(Employee, user=request.user)
        print(employee)

    context = {
        'employees': employees, 
        'employee': employee
    }

    return render(request, "employee/home.html", context)

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            
            messages.success(
                request, 
                f"Employee '{employee.name}' added successfully! His Username: {employee.emp_id}, and deafult Password: {employee.emp_id} also created !"
            )
            return redirect('home')
    else:
        form = EmployeeForm()
    context = {
        'form': form
    }

    return render(request, "employee/add.html", context)


@login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)

    context = {
        'form': form, 'employee': employee
    }

    return render(request, "employee/update.html", context)


@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request, 'employee/delete.html', {'employee': employee})



@login_required
def change_password(request):
    employee = None
    if not request.user.is_superuser:
        employee = get_object_or_404(Employee, empID=request.user.username)
        
    if request.method == 'POST':
        password_form = PasswordChangeForm(data=request.POST, user=request.user)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Keep user logged in after password change
            messages.success(request, f"Password changed successfully!")
            return redirect('home')
    else:
        password_form = PasswordChangeForm(user=request.user)
    
    return render(request, 'employee/change_password.html', {'password_form': password_form, 'employee': employee})
