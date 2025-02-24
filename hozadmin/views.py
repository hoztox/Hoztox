from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_http_methods
from datetime import date, timedelta
import logging
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.db import transaction



 
def employee_profile(request):
    return render(request, 'hozadmin/employee-profile.html')

def client_profile(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'hozadmin/profile.html', {'client': client})



def team_leader(request):
    return render(request, 'hozadmin/team-leader.html')



def client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Client successfully added.")
            return redirect('clients') 
        else:
            messages.error(request, "There was an error with the form. Please check your input.")

            if form.errors.get('email'):
                messages.error(request, "Please provide a valid email address.")
            if form.errors.get('phone'):
                messages.error(request, "Please provide a valid phone number.")

    else:
        form = ClientForm()

 
    clients = Client.objects.all()

    
     

    latest_client = clients.last() if clients.exists() else None  

    return render(request, 'hozadmin/ourclients.html', {'form': form, 'clients': clients, 'latest_client': latest_client})


 
 
def clientupdate(request, client_id=None):
    if client_id:
        client = get_object_or_404(Client, id=client_id)
        print("Client ID:", client_id)
        print("Fetched Client:", client)
        print("Client Logo:", client.logo.url if client.logo else "No logo found")
    else:
        client = None

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            print("Saving client:", client)
            client.save()

            messages.success(request, "Client successfully updated." if client_id else "Client successfully added.")
            return redirect('clients')
        else:
            messages.error(request, "Form validation failed.")
            print("Form errors:", form.errors)  

    else:
        form = ClientForm(instance=client)
        print("Form initial data on GET request:", form.initial)

    clients = Client.objects.all()

    return render(request, 'hozadmin/ourclients.html', {
        'form': form,
        'clients': clients,
        'client_id': client.id if client else None  
    })


 

def delete_client(request, client_id):
    print("Attempting to delete client with ID:", client_id)
    try:
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        print("Client not found.")
        messages.error(request, "Client not found.")
        return redirect('clients') 

    if request.method == "POST":
        client.delete()
        messages.success(request, "Client deleted successfully!")
        return redirect('clients') 
    
    return render(request, 'hozadmin/ourclients.html')



 

def search_clients(request):
    query = request.GET.get('q', '')  
    if query:
   
        clients = Client.objects.filter(
            Q(contact_person__icontains=query) | Q(company_name__icontains=query)
        )
    else:
        clients = Client.objects.all()   

   
    results = [{
        'contact_person': client.contact_person,
        'company_name': client.company_name,
        'email': client.email,
        'phone': client.phone,
        'logo': client.get_logo_url()
    } for client in clients]

    return JsonResponse(results, safe=False)







logger = logging.getLogger(__name__)

def create_project(request):
    if request.method == "POST":
        logger.info("Received project creation request")
        
        try:
            with transaction.atomic():
                # Log received data
                logger.debug(f"POST data: {request.POST}")
                logger.debug(f"FILES data: {request.FILES}")

                # Validate required fields
                name = request.POST.get('projectName')
                if not name:
                    raise ValidationError("Project name is required")

                # Get client
                client_id = request.POST.get('client')
                client = None
                if client_id:
                    try:
                        client = Client.objects.get(id=client_id)
                    except Client.DoesNotExist:
                        raise ValidationError("Selected client does not exist")

                # Create project object
                project = Project(
                    name=name,
                    category=request.POST.get('projectCategory'),
                    client=client,
                    project_lead=request.POST.get('projectLead'),
                    start_date=request.POST.get('projectStartDate') or None,
                    end_date=request.POST.get('projectEndDate') or None,
                    priority=request.POST.get('priority'),
                    description=request.POST.get('description')
                )

                # Validate the model
                project.full_clean()

                # Handle logo
                if 'projectLogo' in request.FILES:
                    project.logo = request.FILES['projectLogo']

                # Save the project
                project.save()
                
                logger.info(f"Project created successfully with ID: {project.id}")
                
                return JsonResponse({
                    "success": True,
                    "message": "Project created successfully",
                    "project_id": project.id
                })

        except ValidationError as e:
            logger.error(f"Validation error: {str(e)}")
            return JsonResponse({
                "success": False,
                "error": str(e)
            }, status=400)
            
        except Exception as e:
            logger.error(f"Unexpected error in project creation: {str(e)}", exc_info=True)
            return JsonResponse({
                "success": False,
                "error": f"Server error: {str(e)}"
            }, status=500)

    return JsonResponse({
        "success": False,
        "error": "Invalid request method"
    }, status=405)



def get_clients(request):

    clients = Client.objects.all().values('id', 'company_name', 'logo')
    return JsonResponse(list(clients), safe=False)

 

def project_list(request):
    all_projects = Project.objects.all()  
    
    # Debugging: Print all projects with their statuses
    for project in all_projects:
        print(f"Project: {project.name}, Status: {project.status}")

    upcoming_projects = Project.objects.filter(status="Up Coming")
    ongoing_ui_projects = Project.objects.filter(status="On Going UI")
    ongoing_dev_projects = Project.objects.filter(status="On Going Dev")
    completed_projects = Project.objects.filter(status="Completed")

    return render(request, 'hozadmin/projects.html', {
        'all_projects': all_projects,   
        'upcoming_projects': upcoming_projects,
        'ongoing_ui_projects': ongoing_ui_projects,
        'ongoing_dev_projects': ongoing_dev_projects,
        'completed_projects': completed_projects,
    })



def get_projects(request):

    projects = Project.objects.all().values('id', 'name', 'logo')
    return JsonResponse(list(projects), safe=False)
 

def get_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    data = {
        "id": project.id,
        "name": project.name,
        "category": project.category,
        "client": {
            "id": project.client.id if project.client else None,
            "company_name": project.client.company_name if project.client else "No Client",
        },
        "project_lead": project.project_lead,
        "logo": project.logo.url if project.logo else None,
        "start_date": project.start_date.strftime("%Y-%m-%d") if project.start_date else "",
        "end_date": project.end_date.strftime("%Y-%m-%d") if project.end_date else "",
        "priority": project.priority,
        "description": project.description,
    }

    return JsonResponse(data)


@require_http_methods(["POST"])
def update_project(request, project_id):
    try:
        project = get_object_or_404(Project, id=project_id)
        
        # Update project fields
        project.name = request.POST.get('name', project.name)
        project.category = request.POST.get('category', project.category)
        project.client_id = request.POST.get('client', project.client_id)
        project.project_lead = request.POST.get('project_lead', project.project_lead)
        project.start_date = request.POST.get('start_date', project.start_date)
        project.end_date = request.POST.get('end_date', project.end_date)
        project.priority = request.POST.get('priority', project.priority)
        project.description = request.POST.get('description', project.description)
        
        # Handle logo upload
        if 'logo' in request.FILES:
            project.logo = request.FILES['logo']
        
        project.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Project updated successfully'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
# Add this to your views.py file

from django.contrib.auth.decorators import login_required

@login_required
def update_project_status(request, project_id):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
    try:
        project = Project.objects.get(id=project_id)
        new_status = request.POST.get('status')
        
        if not new_status:
            return JsonResponse({'success': False, 'error': 'Status is required'})
            
        project.status = new_status
        project.save()
        
        return JsonResponse({'success': True})
    except Project.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Project not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
    
def delete_project(request, project_id):
    if request.method == 'POST':
        try:
            project = Project.objects.get(id=project_id)
            project.delete()
            return JsonResponse({'success': True})
        except Project.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Project not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})




from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Client, Project
from datetime import date


@login_required
def client_profile(request, client_id):
    try:
        client = get_object_or_404(Client, id=client_id)
        
        # Get all projects for this client
        projects = Project.objects.filter(client=client).order_by('-start_date')
        
        # Filter projects by status
        ongoing_projects = projects.filter(
            status__in=['On Going UI', 'On Going Dev']
        )
        completed_projects = projects.filter(status='Completed')
        upcoming_projects = projects.filter(status='Up Coming')
        
        context = {
            'client': client,
            'ongoing_projects': ongoing_projects,
            'completed_projects': completed_projects,
            'upcoming_projects': upcoming_projects,
            'total_projects': projects.count(),
        }
        
        return render(request, 'hozadmin/profile.html', context)
        
    except Exception as e:
        print(f"Error in client_profile: {str(e)}")
        messages.error(request, f"An error occurred while loading client profile: {str(e)}")
        return redirect('client_list')

def search_projects(request, client_id):
    try:
        client = get_object_or_404(Client, id=client_id)
        query = request.GET.get('q', '')
        
        if query:
            projects = Project.objects.filter(
                client=client
            ).filter(
                Q(name__icontains=query) |
                Q(category__icontains=query) |
                Q(status__icontains=query) |
                Q(project_lead__icontains=query)
            )
        else:
            projects = Project.objects.filter(client=client)
        
        return render(request, 'hozadmin/project_search_results.html', {
            'client': client,
            'projects': projects,
            'query': query
        })
        
    except Exception as e:
        messages.error(request, f"Error during search: {str(e)}")
        return redirect('client_projects', client_id=client_id)
    


@login_required
def client_projects_view(request, client_id):
    try:
        client = get_object_or_404(Client, id=client_id)

        # Ongoing projects
        ongoing_projects = Project.objects.filter(
            client=client,
            status__in=['On Going UI', 'On Going Dev']
        ).order_by('-start_date')

        # Completed projects
        completed_projects = Project.objects.filter(
            client=client,
            status='Completed'
        ).order_by('-start_date')

        # Upcoming projects
        upcoming_projects = Project.objects.filter(
            client=client,
            status='Up Coming'
        ).order_by('-start_date')

        # All projects
        all_projects = Project.objects.filter(client=client).order_by('-start_date')

        # Project stats
        stats = {
            'total_projects': all_projects.count(),
            'ongoing_ui': ongoing_projects.filter(status='On Going UI').count(),
            'ongoing_dev': ongoing_projects.filter(status='On Going Dev').count(),
            'completed': completed_projects.count(),
            'upcoming': upcoming_projects.count(),
        }

        # Pagination for ongoing projects
        paginator = Paginator(ongoing_projects, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'client': client,
            'ongoing_projects': page_obj,
            'completed_projects': completed_projects,  # ✅ Add completed projects
            'upcoming_projects': upcoming_projects,
            'stats': stats,
        }

        return render(request, 'hozadmin/client_projects.html', context)

    except Exception as e:
        print(f"Error in client_projects_view: {str(e)}")
        messages.error(request, f"An error occurred while loading projects: {str(e)}")
        return redirect('client_list')


def employee_list(request):
    form = EmployeeForm()
    employees = Employee.objects.all()
    context = {
        'employees': employees,
        'form': form,
    }
    return render(request, 'hozadmin/members.html', context)

from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
@require_POST
def create_employee(request):
    print("Form data received:", request.POST)
    print("Files received:", request.FILES)
    
  
    if not request.POST and not request.FILES:
        return JsonResponse({'success': False, 'html': '<p>No data received</p>'})
    
    form = EmployeeForm(request.POST, request.FILES)
    print("Form bound:", form.is_bound)
    
    if form.is_valid():
        try:
            employee = form.save()
            print("Employee saved successfully:", employee)
            return JsonResponse({'success': True})
        except Exception as e:
            print("Error saving employee:", str(e))
            return JsonResponse({'success': False, 'html': f'<p>Error saving: {str(e)}</p>'})
    else:
        print("Form is invalid. Errors:", form.errors)
        errors_html = '<ul>'
        for field, errors in form.errors.items():
            for error in errors:
                errors_html += f'<li>{field}: {error}</li>'
        errors_html += '</ul>'
        return JsonResponse({'success': False, 'html': errors_html})

def employee_profile(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'hozadmin/employee-profile.html', {'employee': employee})

def update_employee_personal_info(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeePersonalInfoForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal information updated successfully.')
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def update_employee_bank_info(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeBankInfoForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bank information updated successfully.')
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def update_employee_basic_info(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeBasicInfoForm(request.POST, instance=employee)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({'status': 'success'})
            except Exception as e:
                return JsonResponse({
                    'status': 'error',
                    'errors': {'server': str(e)}
                })
        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        })
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    })


def employee_profile(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    personal_form = EmployeePersonalInfoForm(instance=employee)
    bank_form = EmployeeBankInfoForm(instance=employee)
    basic_form = EmployeeBasicInfoForm(instance=employee)
    
    context = {
        'employee': employee,
        'personal_form': personal_form,
        'bank_form': bank_form,
        'basic_form': basic_form,
    }
    return render(request, 'hozadmin/employee-profile.html', context)

  
from django.utils.timezone import now
 

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.timezone import now
from .models import Task, Project, Employee

from django.utils.timezone import now
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task, Project, Employee

def tasks(request):
    today = now().date()

    # Fetch tasks based on project category
    uiux_tasks = Task.objects.filter(project__category='UI/UX Design')
    web_dev_tasks = Task.objects.filter(project__category='Website Development')
    seo_tasks = Task.objects.filter(project__category='SEO')
    social_media_tasks = Task.objects.filter(project__category='Social Media')

    # Categorizing tasks for UI/UX
    uiux_upcoming = uiux_tasks.filter(start_date__gt=today)
    uiux_ongoing = uiux_tasks.filter(start_date__lte=today, end_date__gte=today)
    uiux_completed = uiux_tasks.filter(end_date__lt=today)

    # Categorizing tasks for Website Development
    web_dev_upcoming = web_dev_tasks.filter(start_date__gt=today)
    web_dev_ongoing = web_dev_tasks.filter(start_date__lte=today, end_date__gte=today)
    web_dev_completed = web_dev_tasks.filter(end_date__lt=today)

    # Categorizing tasks for SEO
    seo_upcoming = seo_tasks.filter(start_date__gt=today)
    seo_ongoing = seo_tasks.filter(start_date__lte=today, end_date__gte=today)
    seo_completed = seo_tasks.filter(end_date__lt=today)

    # Categorizing tasks for Social Media
    social_upcoming = social_media_tasks.filter(start_date__gt=today)
    social_ongoing = social_media_tasks.filter(start_date__lte=today, end_date__gte=today)
    social_completed = social_media_tasks.filter(end_date__lt=today)

    if request.method == 'POST':
        name = request.POST.get('name')
        project_id = request.POST.get('project')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        priority = request.POST.get('priority')
        description = request.POST.get('description', '')
        assigned_users = request.POST.getlist('assigned_users')

        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            messages.error(request, "Project not found!")
            return redirect('tasks')

        task = Task(
            name=name,
            project=project,
            start_date=start_date,
            end_date=end_date,
            priority=priority,
            description=description
        )
        task.save()
        task.assigned_employees.set(assigned_users)

        if request.FILES.get('attachments'):
            task.attachments = request.FILES['attachments']
            task.save()

        messages.success(request, "Task created successfully!")
        return redirect('tasks')

    context = {
        'uiux_upcoming': uiux_upcoming,
        'uiux_ongoing': uiux_ongoing,
        'uiux_completed': uiux_completed,
        'web_dev_upcoming': web_dev_upcoming,
        'web_dev_ongoing': web_dev_ongoing,
        'web_dev_completed': web_dev_completed,
        'seo_upcoming': seo_upcoming,
        'seo_ongoing': seo_ongoing,
        'seo_completed': seo_completed,
        'social_upcoming': social_upcoming,
        'social_ongoing': social_ongoing,
        'social_completed': social_completed,
        'projects': Project.objects.all().order_by('name'),
        'employees': Employee.objects.all().order_by('name')
    }

    return render(request, 'hozadmin/taskpage.html', context)


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.name = request.POST.get("name")
        task.project_id = request.POST.get("project")
        task.start_date = request.POST.get("start_date")
        task.end_date = request.POST.get("end_date")
        task.priority = request.POST.get("priority")
       
        task.description = request.POST.get("description")

      
        employee_ids = request.POST.getlist("assigned_employees")
        task.assigned_employees.set(employee_ids)

        if "attachments" in request.FILES:
            task.attachments = request.FILES["attachments"]

        task.save()
        messages.success(request, "Task updated successfully!")
        return redirect("tasks")

    return render(request, "hozadmin/taskpage.html", {"task": task})



from django.utils import timezone
from datetime import date


 
from datetime import date
from django.shortcuts import render
from .models import Task, Project

from datetime import date
from django.shortcuts import render
from .models import Project, Task

def home(request):
    today = date.today()
    
    # Get all projects
    all_projects = Project.objects.all().order_by('-start_date')
    
    # Filter projects by status
    upcoming_projects = all_projects.filter(status='Up Coming')
    ongoing_projects = all_projects.filter(status__startswith='On Going')
    completed_projects = all_projects.filter(status='Completed')

    # Calculate completion percentage for each project
    for project in all_projects:
        if project.end_date and project.start_date:
            total_days = (project.end_date - project.start_date).days
            days_passed = (today - project.start_date).days
            project.completion_percentage = round(
                min(100, max(0, (days_passed / total_days) * 100)), 1
            ) if total_days > 0 else 0
        else:
            project.completion_percentage = 0

    # Task calculations
    tasks = Task.objects.all()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(end_date__lt=today).count()
    progress_tasks = tasks.filter(start_date__lte=today, end_date__gte=today).count()
    pending_tasks = tasks.filter(start_date__gt=today).count()

    context = {
        # Projects data
        'all_projects': all_projects,
        'upcoming_projects': upcoming_projects,
        'ongoing_projects': ongoing_projects,
        'completed_projects': completed_projects,
        'total_projects': all_projects.count(),
        'upcoming_count': upcoming_projects.count(),
        'ongoing_count': ongoing_projects.count(),
        'completed_count': completed_projects.count(),
        # Task data
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'progress_tasks': progress_tasks,
        'pending_tasks': pending_tasks,
    }
    
    return render(request, 'hozadmin/index.html', context)



 