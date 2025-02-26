from django.db import models

class Client(models.Model):
    contact_person = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    service = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='client_logos/', null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null =True,blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name or str(self.contact_person)

    def get_logo_url(self):
        if self.logo:
            return self.logo.url
        return None 

from datetime import datetime, date
class Project(models.Model):

    PROJECT_CATEGORIES = [
        ('UI/UX Design', 'UI/UX Design'),
        ('Website Development', 'Website Development'),       
        ('SEO', 'SEO'),
        ('Social Media', 'Social Media'),
    ]
    PRIORITY = [
        ('Highest', 'Highest'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Lowest', 'Lowest')
    ]
    STATUS_CHOICES = [
        ('Up Coming', 'Up Coming'),
        ('On Going UI', 'On Going UI'),
        ('On Going Dev' ,'On Going Dev'),     
        ('Completed', 'Completed'),
        
    ]
    name = models.CharField(max_length=255,blank=True,unique=True ,null=True)
    category = models.CharField(max_length=255, choices=PROJECT_CATEGORIES,blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects',blank=True, null=True)
    project_lead = models.CharField(max_length=255,blank=True, null=True)
    logo = models.ImageField(upload_to='project_logos/', null=True, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)   
    priority = models.CharField(max_length=255, choices=PRIORITY,blank=True, null=True)
    status =  models.CharField(max_length=255, choices=STATUS_CHOICES , default='Up Coming',blank=True, null=True)
    days_remaining = models.IntegerField(null=True,blank=True)
    description = models.TextField(blank=True, null=True)

    def days_remaining(self):
        if not self.end_date:
            return "No deadline"
        
        today = date.today()
        if self.end_date < today:
            return "Overdue"
            
        delta = self.end_date - today
        return f"{delta.days}"

    def __str__(self):
        return self.name if self.name else f"Project {self.id}"
    
 

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('IT Management', 'IT Management'),
        ('Marketing', 'Marketing'),
    ]

    DESIGNATIONS = [
        ('UI/UX Design', 'UI/UX Design'),
        ('Website Development', 'Website Development'),       
        ('SEO', 'SEO'),
        ('Social Media', 'Social Media'),
         
    ]

    name = models.CharField(max_length=15, null=True, blank=True, verbose_name="Full Name")
    employee_id = models.CharField(max_length=255, blank=True, unique=True, null=True, verbose_name="Employee ID")
    join_date = models.DateField(null=True, blank=True, verbose_name="Joining Date")
    username = models.CharField(max_length=15, null=True, blank=True)
    password = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=200, choices=DEPARTMENT_CHOICES, null=True, blank=True)
    designation = models.CharField(max_length=200, choices=DESIGNATIONS, null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name="Job Description")
    nationality = models.CharField(max_length=15, null=True, blank=True)
    address =  models.TextField(blank=True, null=True, verbose_name="Address")
    religion = models.CharField(max_length=15, null=True, blank=True)
    marital_status = models.CharField(max_length=15, null=True, blank=True)
    emergency_contact = models.CharField(max_length=15, null=True, blank=True)
    logo = models.ImageField(upload_to='employee_logos/', null=True, blank=True)
    bank_name = models.CharField(max_length=15, null=True, blank=True)
    acc_no = models.CharField(max_length=15, null=True, blank=True, verbose_name="Account Number")
    ifsc = models.CharField(max_length=15, null=True, blank=True, verbose_name="IFSC Code")
    pan = models.CharField(max_length=15, null=True, blank=True, verbose_name="PAN Number")
    phone =  models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    upi_id = models.CharField(max_length=15, null=True, blank=True, verbose_name="UPI ID")

    def __str__(self):
        return self.name or str(self.employee_id)

from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Highest', 'Highest'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Lowest', 'Lowest')
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=255, null=False, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_employees = models.ManyToManyField(Employee, related_name='tasks')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    description = models.TextField(null=True, blank=True)
    attachments = models.FileField(upload_to='task_files/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.project.name}"
    

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Unique related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Unique related_name
        blank=True,
    )

    objects = MyAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.email
