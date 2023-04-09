from django.urls import path, include
from . import views
from myapp.controllers.companyView import add_company

urlpatterns = [
    
    # path('add_person/', views.add_person, name='add_person'),
    # add any other URL patterns for your app here
    path('add_company/', add_company, name='add_company'),
]