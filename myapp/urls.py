# from django.urls import path, include
# from . import views
# from myapp.controllers.Company import add_companies, update_companies, get_companies
# from myapp.controllers.Employee import add_employees,show_employees, update_employees
# urlpatterns = [
    
#     # path('add_person/', views.add_person, name='add_person'),
#     # add any other URL patterns for your app here
#     path('api/companies/', add_companies, name='add_companies'),
#     path('api/companies/<int:id>/', update_companies, name='update_companies'),
#     path('api/companies/<int:id>/', get_companies, name='get_companies'),
    

#     path('api/employees/<int:id>/', add_employees, name='add_employees'),
#      path('api/employees/update/<int:id>/<int:emp_id>/', update_employees, name='update_employees'),
#     path('api/employees/show/<int:id>/', show_employees, name='show_employees'),

# ]

from django.urls import path, include
from rest_framework import routers
from myapp.controllers.Company import CompanyViewSet
# from myapp.controllers.Employee import Employee

router = routers.SimpleRouter()
router.register(r'companies', CompanyViewSet, basename='CompanyViewSet')
# router.register(r'employees', Employee)

urlpatterns = [
    path('api/', include(router.urls)),
]
