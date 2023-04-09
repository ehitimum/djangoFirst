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
from myapp.controllers.Employee import EmployeeViewSet


# router = routers.SimpleRouter()
# router.register(r'companies', CompanyViewSet, basename='CompanyViewSet')

# # Define a nested router for employees under the companies router
# companies_router = routers.DefaultRouter()
# companies_router.register(r'employees', EmployeeViewSet, basename='EmployeeViewSet')

# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('api/companies/<int:id>/', include(companies_router.urls)),
#      path('api/companies/<int:company_id>/employees/', EmployeeViewSet.as_view({'get': 'app_employees'}), name='app_employees'),
# ]
router = routers.SimpleRouter()
router.register(r'companies', CompanyViewSet, basename='CompanyViewSet')
router.register(r'employees', EmployeeViewSet, basename='EmployeeViewSet')

urlpatterns = [
    # path('api/', include(router.urls)),
    path('api/', include(router.urls)),
]




# company_list = CompanyViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# company_detail = CompanyViewSet.as_view({
#     'get':'get_companies', 
#     'put':'update_compaines'
# })

# employee_detail = EmployeeViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy'
# })

# urlpatterns = [
#     path('api/companies/', CompanyViewSet.as_view({'post':'add_companies'}), name='add-companies'),
#     path('api/companies/<int:pk>/', company_detail, name='company-detail'),
#     path('api/companies/<int:id>/employees/', EmployeeViewSet.as_view({'post': 'add_employees'}), name='add-employee'),
    
# ]

# urlpatterns = [
#     path('companies/', company_list, name='company-list'),
#     path('companies/<int:pk>/', company_detail, name='company-detail'),
#     path('companies/<int:pk>/add_employee/', EmployeeViewSet.as_view({'post': 'add_employee'}), name='add-employee'),
#     path('employees/<int:pk>/', employee_detail, name='employee-detail'),
# ]