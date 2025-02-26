from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['contact_person', 'company_name', 'service', 'logo', 'email','address', 'phone','address', 'description']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'category', 'client', 'project_lead', 'logo', 'start_date', 'end_date', 'priority', 'description']

    client = forms.ModelChoiceField(queryset=Client.objects.all(), empty_label="Select Client")

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(render_value=True),
            'description': forms.Textarea(attrs={'rows': 3}),
            'employee_id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
class EmployeePersonalInfoForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['nationality', 'religion', 'marital_status', 'emergency_contact']
        widgets = {
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'religion': forms.TextInput(attrs={'class': 'form-control'}),
            'marital_status': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EmployeeBankInfoForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['bank_name', 'acc_no', 'ifsc', 'pan', 'upi_id']
        widgets = {
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'acc_no': forms.TextInput(attrs={'class': 'form-control'}),
            'ifsc': forms.TextInput(attrs={'class': 'form-control'}),
            'pan': forms.TextInput(attrs={'class': 'form-control'}),
            'upi_id': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EmployeeBasicInfoForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'designation', 'join_date', 'address', 'description','phone','email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'join_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),           
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'project', 'assigned_employees', 'start_date', 'end_date', 'priority', 'status', 'description', 'attachments']

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'employees': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            
        }


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'name@company.com',
            'autocomplete': 'email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'autocomplete': 'current-password'
        })
    )
    remember_me = forms.BooleanField(required=False)
