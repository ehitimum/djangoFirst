from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    company_id = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    employee_title = models.CharField(max_length=200)
    employee_contact_info = models.CharField(max_length=200)

    class Meta:
        app_label = 'myapp'
        db_table = 'employee'