from django.db import models
from myapp.modelss.Company import Company
from myapp.modelss.Employee import Employee
from myapp.modelss.Device import Device

class Device_Log(models.Model):
    id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    checkout_time = models.DateTimeField()
    return_time = models.DateTimeField()
    checkout_condition = models.CharField(max_length=100)
    return_condition = models.CharField(max_length=200)
    

    class Meta:
        app_label = 'myapp'
        db_table = 'device_log'