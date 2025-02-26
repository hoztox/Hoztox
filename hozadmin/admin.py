from django.contrib import admin
from .models import * 

class ClientAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_person', 'email', 'phone','address']
    search_fields = ['company_name', 'contact_person']
admin.site.register(Client)

 


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'client', 'start_date', 'end_date', 'priority')  
    search_fields = ['name', 'client']
admin.site.register(Project)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department', 'designation', 'join_date','phone','email')
    list_filter = ('department', 'designation', 'marital_status')
    search_fields = ('name', 'employee_id', 'department', 'designation')
    readonly_fields = ('employee_id',)
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'username', 'password', 'nationality', 'religion', 'marital_status', 'emergency_contact','logo','address')
        }),
        ('Job Details', {
            'fields': ('employee_id', 'join_date', 'department', 'designation', 'description','phone','email')
        }),
        ('Banking & ID Details', {
            'fields': ('bank_name', 'acc_no', 'ifsc', 'pan', 'upi_id')
        }),
    )
admin.site.register(Employee)

admin.site.register(Task)