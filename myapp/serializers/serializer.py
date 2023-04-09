from rest_framework import serializers
from myapp.modelss.Company import Company
from myapp.modelss.Employee import Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'company_name', 'company_address']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'employee_name', 'employee_title', 'employee_contact_info', 'company']