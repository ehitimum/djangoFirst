from django.urls import path, include
from . import views
from myapp.controllers.Company import add_companies, update_companies, get_companies
from myapp.controllers.Employee import add_employee
urlpatterns = [
    
    # path('add_person/', views.add_person, name='add_person'),
    # add any other URL patterns for your app here
    path('api/companies/', add_companies, name='add_companies'),
    path('api/companies/update/<int:id>/', update_companies, name='update_companies'),
    path('api/companies/<int:id>/', get_companies, name='get_companies'),
    

    path('api/employees', add_employee, name='add_employee'),

]