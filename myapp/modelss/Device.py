from django.db import models
from myapp.modelss.Company import Company
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    device_name = models.CharField(max_length=100)
    device_description = models.CharField(max_length=200)
    

    class Meta:
        app_label = 'myapp'
        db_table = 'device'