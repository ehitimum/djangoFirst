from django.urls import path, include
from . import views
from myapp.controllers.Company import add_companies, update_companies, get_companies
from myapp.controllers.Employee import add_employees,show_employees, update_employees, get_employee_info
from myapp.controllers.Device import add_devices, show_device_list, update_device_info
from myapp.controllers.DeviceLog import add_device_logs, show_device_log, update_device_logs
urlpatterns = [
    
    # path('add_person/', views.add_person, name='add_person'),
    # add any other URL patterns for your app here
    path('api/companies/', add_companies, name='add_companies'),
    path('api/companies/<int:id>/', update_companies, name='update_companies'),
    path('api/companies/<int:id>/', get_companies, name='get_companies'),
    

    path('api/companies/<int:id>/employees/', add_employees, name='add_employees'),
    path('api/companies/<int:id>/employees/<int:emp_id>/', update_employees, name='update_employees'),
    path('api/companies/<int:id>/employees/show/', show_employees, name='show_employees'),
    path('api/companies/<int:id>/employees/<int:emp_id>/show/', get_employee_info, name='get_employee_info'),


    path('api/companies/<int:id>/devices/', add_devices, name='add_devices'),
    path('api/companies/<int:id>/devices/show/', show_device_list, name='show_device_list'),
    path('api/companies/<int:id>/devices/<int:de_id>/', update_device_info, name='update_device_info'),


    path('api/companies/<int:id>/devices/<int:de_id>/device_logs/', add_device_logs, name='add_device_logs'),
    path('api/companies/<int:id>/devices/<int:de_id>/device_logs/show/', show_device_log, name='show_device_log'),
    path('api/companies/<int:id>/devices/<int:de_id>/device_logs/show/<int:log_id>/', update_device_logs, name='update_device_logs'),


]

