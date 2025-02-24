# from django.test import TestCase

# # Create your tests here.


#   <!-- sidebar -->
#     <div class="sidebar px-4 py-4 py-md-5 me-0">
#         <div class="d-flex flex-column h-100">
#             <a href="" class="mb-0 brand-icon hoztox-logo">               
#                     <img src="{% static 'assets/images/hoztox-logo.svg' %}">             
#             </a>
#             <!-- Menu: main ul -->

#             <ul class="menu-list flex-grow-1 mt-3">             
#                 <li><a class="m-link" href=" "><i class="icofont-home fs-5"></i> <span>Dashboard</span></a></li>
#                 <li  class="collapsed">
#                     <a class="m-link"  data-bs-toggle="collapse" data-bs-target="#project-Components" href="#">
#                         <i class="icofont-briefcase"></i><span>Projects</span> <span class="arrow icofont-dotted-down ms-auto text-end fs-5"></span></a>
#                     <!-- Menu: Sub menu ul -->
#                     <ul class="sub-menu collapse" id="project-Components">
#                         <li><a class="ms-link" href="projects"><span>Projects</span></a></li>
#                         <li><a class="ms-link" href="{% url 'tasks' %}"><span>Tasks</span></a></li>
#                         <!-- <li><a class="ms-link" href="timesheet.html"><span>Timesheet</span></a></li> -->
#                         <li><a class="ms-link" href="{% url 'leader' %}"><span>Leaders</span></a></li>
#                     </ul>
#                 </li>               
#                 <li class="collapsed">
#                     <a class="m-link" data-bs-toggle="collapse" data-bs-target="#client-Components" href="#"><i
#                             class="icofont-user-male"></i> <span>Our Clients</span> <span class="arrow icofont-dotted-down ms-auto text-end fs-5"></span></a>
#                     <!-- Menu: Sub menu ul -->
#                     <ul class="sub-menu collapse" id="client-Components">
#                         <li><a class="ms-link" href="ourclients.html"> <span>Clients</span></a></li>
#                         <li><a class="ms-link" href="profile.html"> <span>Client Profile</span></a></li>
#                     </ul>
#                 </li>
#                 <li class="collapsed">
#                     <a class="m-link" data-bs-toggle="collapse" data-bs-target="#emp-Components" href="#"><i
#                             class="icofont-users-alt-5"></i> <span>Employees</span> <span class="arrow icofont-dotted-down ms-auto text-end fs-5"></span></a>
#                     <!-- Menu: Sub menu ul -->
#                     <ul class="sub-menu collapse" id="emp-Components">
#                         <li><a class="ms-link" href="members.html"> <span>Members</span></a></li>
#                         <li><a class="ms-link" href="employee-profile.html"> <span>Members Profile</span></a></li>                       
#                     </ul>
#                 </li>             
#             </ul>           
#             <!-- Menu: menu collepce btn -->
#             <button type="button" class="btn btn-link sidebar-mini-btn text-light">
#                 <span class="ms-2"><i class="icofont-bubble-right"></i></span>
#             </button>
#         </div>
#     </div>






#    <!-- Body: Header -->
#         <div class="header">
#             <nav class="navbar py-4">
#                 <div class="container-xxl">    
#                     <!-- header rightbar icon -->
#                     <div class="h-right d-flex align-items-center mr-5 mr-lg-0 order-1">                      
#                         <div class="dropdown user-profile ml-2 ml-sm-3 d-flex align-items-center">
#                             <div class="u-info me-2">
#                                 <p class="mb-0 text-end line-height-sm "><span class="font-weight-bold">Rasheed</span></p>
#                                 <small>Admin Profile</small>
#                             </div>
#                             <a class="nav-link dropdown-toggle pulse p-0" href="#" role="button" data-bs-toggle="dropdown" data-bs-display="static">
#                                 <img class="avatar lg rounded-circle img-thumbnail" src="{% static 'assets/images/Rasheed-12.webp' %}" alt="profile">
#                             </a>
#                             <div class="dropdown-menu rounded-lg shadow border-0 dropdown-animation dropdown-menu-end p-0 m-0">
#                                 <div class="card border-0 w280">
#                                     <div class="card-body pb-0">
#                                         <div class="d-flex py-1">
#                                             <img class="avatar rounded-circle" src="{% static 'assets/images/profile_av.png' %}" alt="profile">
#                                             <div class="flex-fill ms-3">
#                                                 <p class="mb-0"><span class="font-weight-bold">Dylan Hunter</span></p>
#                                                 <small class="">Dylan.hunter@gmail.com</small>
#                                             </div>
#                                         </div>
                                        
#                                         <div><hr class="dropdown-divider border-dark"></div>
#                                     </div>
#                                     <div class="list-group m-2 ">
#                                         <a href="task.html" class="list-group-item list-group-item-action border-0 "><i class="icofont-tasks fs-5 me-3"></i>My Task</a>
#                                         <a href="members.html" class="list-group-item list-group-item-action border-0 "><i class="icofont-ui-user-group fs-6 me-3"></i>members</a>
#                                         <a href="ui-elements/auth-signin.html" class="list-group-item list-group-item-action border-0 "><i class="icofont-logout fs-6 me-3"></i>Signout</a>
#                                         <div><hr class="dropdown-divider border-dark"></div>
#                                         <a href="ui-elements/auth-signup.html" class="list-group-item list-group-item-action border-0 "><i class="icofont-contact-add fs-5 me-3"></i>Add personal account</a>
#                                     </div>
#                                 </div>
#                             </div>
#                         </div>
#                         <div class="px-md-1">
#                             <a href="#offcanvas_setting" data-bs-toggle="offcanvas" aria-expanded="false" title="template setting">
#                                 <svg class="svg-stroke" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
#                                     <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
#                                     <path d="M10.325 4.317c.426 -1.756 2.924 -1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543 -.94 3.31 .826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756 .426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543 -.826 3.31 -2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756 -2.924 1.756 -3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543 .94 -3.31 -.826 -2.37 -2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756 -.426 -1.756 -2.924 0 -3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94 -1.543 .826 -3.31 2.37 -2.37c1 .608 2.296 .07 2.572 -1.065z"></path>
#                                     <path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0"></path>
#                                 </svg>
#                             </a>
#                         </div>
#                     </div>
    
#                     <!-- menu toggler -->
#                     <button class="navbar-toggler p-0 border-0 menu-toggle order-3" type="button" data-bs-toggle="collapse" data-bs-target="#mainHeader">
#                         <span class="fa fa-bars"></span>
#                     </button>
    
#                     <!-- main menu Search-->
#                     <div class="order-0 col-lg-4 col-md-4 col-sm-12 col-12 mb-3 mb-md-0 ">
#                         <div class="input-group flex-nowrap input-group-lg">
#                             <button type="button" class="input-group-text" id="addon-wrapping"><i class="fa fa-search"></i></button>
#                             <input type="search" class="form-control" placeholder="Search" aria-label="search" aria-describedby="addon-wrapping">
#                             <button type="button" class="input-group-text add-member-top" id="addon-wrappingone" data-bs-toggle="modal" data-bs-target="#addUser"><i class="fa fa-plus"></i></button>
#                         </div>
#                     </div>
    
#                 </div>
#             </nav>
#         </div>



#    <!-- Edit Project-->
#         <div class="modal fade" id="editproject" tabindex="-1"  aria-hidden="true">
#             <div class="modal-dialog modal-dialog-centered modal-md modal-dialog-scrollable">
#             <div class="modal-content">
#                 <div class="modal-header">
#                     <h5 class="modal-title  fw-bold" id="editprojectLabel"> Edit Project</h5>
#                     <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
#                 </div>
#                 <div class="modal-body">
#                     <div class="mb-3">
#                         <label for="exampleFormControlInput78" class="form-label">Project Name</label>
#                         <input type="text" class="form-control" id="exampleFormControlInput78" value="Social Geek Made">
#                     </div>
#                     <div class="mb-3">
#                         <label  class="form-label">Project Category</label>
#                         <select class="form-select" aria-label="Default select example">
#                             <option selected>UI/UX Design</option>
#                             <option value="1">Website Design</option>
#                             <option value="2">App Development</option>
#                             <option value="3">Quality Assurance</option>
#                             <option value="4">Development</option>
#                             <option value="5">Backend Development</option>
#                             <option value="6">Software Testing</option>
#                             <option value="7">Website Design</option>
#                             <option value="8">Marketing</option>
#                             <option value="9">SEO</option>
#                             <option value="10">Other</option>
#                         </select>
#                     </div>
#                     <div class="mb-3">
#                         <label for="formFileMultiple456" class="form-label">Project Images & Document</label>
#                         <input class="form-control" type="file" id="formFileMultiple456">
#                     </div>
#                     <div class="deadline-form">
#                         <form>
#                             <div class="row g-3 mb-3">
#                               <div class="col">
#                                 <label for="datepickerded123" class="form-label">Project Start Date</label>
#                                 <input type="date" class="form-control" id="datepickerded123" value="2021-01-10">
#                               </div>
#                               <div class="col">
#                                 <label for="datepickerded456" class="form-label">Project End Date</label>
#                                 <input type="date" class="form-control" id="datepickerded456" value="2021-04-10">
#                               </div>
#                             </div>
#                             <div class="row g-3 mb-3">
#                                 <div class="col-sm-12">
#                                     <label class="form-label">Notifation Sent</label>
#                                     <select class="form-select" aria-label="Default select example">
#                                         <option selected>All</option>
#                                         <option value="1">Team Leader Only</option>
#                                         <option value="2">Team Member Only</option>
#                                     </select>
#                                 </div>
#                                 <div class="col-sm-12">
#                                     <label for="formFileMultipleone" class="form-label">Task Assign Person</label>
#                                     <select class="form-select" multiple aria-label="Default select Priority">
#                                         <option selected>Lucinda Massey</option>
#                                         <option selected value="1">Ryan Nolan</option>
#                                         <option selected value="2">Oliver Black</option>
#                                         <option selected value="3">Adam Walker</option>
#                                         <option selected value="4">Brian Skinner</option>
#                                         <option value="5">Dan Short</option>
#                                         <option value="5">Jack Glover</option>
#                                     </select>
#                                 </div>
#                             </div>
#                         </form>
#                     </div>
#                     <div class="row g-3 mb-3">
#                         <div class="col-sm">
#                             <label for="formFileMultipleone" class="form-label">Priority</label>
#                             <select class="form-select" aria-label="Default select Priority">
#                                 <option selected>Medium</option>
#                                 <option value="1">Highest</option>
#                                 <option value="2">Low</option>
#                                 <option value="3">Lowest</option>
#                             </select>
#                         </div>
#                     </div>
#                     <div class="mb-3">
#                         <label for="exampleFormControlTextarea786" class="form-label">Description (optional)</label>
#                         <textarea class="form-control" id="exampleFormControlTextarea786" rows="3">Social Geek Made,lorem urna commodo sem. Pellentesque venenatis leo quam, sed mattis sapien lobortis ut. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere
#                         </textarea>
#                     </div>
#                 </div>
#                 <div class="modal-footer">
#                     <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Done</button>
#                     <button type="button" class="btn btn-primary">Create</button>
#                 </div>
#             </div>
#             </div>
#         </div>



#   <!-- Modal  Delete Folder/ File-->
#         <div class="modal fade" id="deleteproject" tabindex="-1"  aria-hidden="true">
#             <div class="modal-dialog modal-dialog-centered modal-md modal-dialog-scrollable">
#             <div class="modal-content">
#                 <div class="modal-header">
#                     <h5 class="modal-title  fw-bold" id="deleteprojectLabel"> Delete item Permanently?</h5>
#                     <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
#                 </div>
#                 <div class="modal-body justify-content-center flex-column d-flex">
#                     <i class="icofont-ui-delete text-danger display-2 text-center mt-2"></i>
#                     <p class="mt-4 fs-5 text-center">You can only delete this item Permanently</p>
#                 </div>
#                 <div class="modal-footer">
#                     <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
#                     <button type="button" class="btn btn-danger color-fff">Delete</button>
#                 </div>
#             </div>
#             </div>
#         </div>


#  <!-- Edite projetc status -->

#         <div class="modal fade" id="editprojectstatus" tabindex="-1" aria-hidden="true">
#             <div class="modal-dialog modal-dialog-centered modal-md modal-dialog-scrollable">
#                 <div class="modal-content">
#                     <div class="modal-header">
#                         <h5 class="modal-title fw-bold" id="createprojectlLabel"> Project Status Edit</h5>
#                         <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
#                     </div>
#                     <div class="modal-body">
                      
#                         <div class="mb-3">
#                             <label class="form-label"> Project Status Edit</label>
#                             <select class="form-select" id="projectCategory" aria-label="Select Project Category">
#                                 <option selected>Up Comming</option>
#                                 <option value="1"> On Going</option>
#                                 <option value="2">Completed</option>                                
#                             </select>
#                         </div>                        
#                     </div>
#                     <div class="modal-footer">
#                         <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Done</button>                      
#                     </div>
#                 </div>
#             </div>
#         </div>