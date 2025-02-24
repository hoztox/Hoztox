from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', home, name='home'),  
   
    path('employee-profile/', views.employee_profile, name='employee-profile'),
    path('projects/tasks/', views.tasks, name='tasks'),
    path('projects/leader/',views.team_leader, name='leader'),
    path('clients/', views.client , name = 'clients'),
    path('client/update/<int:client_id>/', clientupdate, name='client_update'),
    path("delete-client/<int:client_id>/", delete_client, name="delete_client"),    
    path('search/', search_clients, name='search_clients'),
    path('create/', views.create_project, name='create_project'),
    path('clients-list/', get_clients, name='get_clients'),
    path('projects/', project_list, name='project_list'),
    path('project-list/', get_projects, name='get_clients'),
    path('projects/<int:project_id>/', views.get_project, name='get_project'),
    path('projects/<int:project_id>/update/', views.update_project, name='update_project'),
    path('projects/<int:project_id>/update-status/', views.update_project_status, name='update_project_status'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),   
    path('client-profile/', views.client_profile, name='client_profile'),  
    path('client-profile/<int:client_id>/', views.client_profile, name='client_profile'),
    path('client/<int:client_id>/projects/', client_projects_view, name='client_projects'),  
    path('employees/', views.employee_list, name='employee_list'),
    path('create-employee/', views.create_employee, name='create_employee'),
    path('employee-profile/<int:employee_id>/', views.employee_profile, name='employee_profile'),
    path('employee/<int:employee_id>/update-personal-info/', views.update_employee_personal_info, name='update-employee-personal-info'),
    path('employee/<int:employee_id>/update-bank-info/', views.update_employee_bank_info, name='update-employee-bank-info'),
    path('employee/<int:employee_id>/update-basic-info/', views.update_employee_basic_info, name='update-employee-basic-info'),
    path('task/edit/<int:task_id>/', edit_task, name='edit_task'),
   
    
    
]
