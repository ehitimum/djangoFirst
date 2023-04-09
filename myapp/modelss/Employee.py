from django.db import models
from myapp.modelss.Company import Company
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    employee_name = models.CharField(max_length=100)
    employee_title = models.CharField(max_length=200)
    employee_contact_info = models.CharField(max_length=200)

    class Meta:
        app_label = 'myapp'
        db_table = 'employee'