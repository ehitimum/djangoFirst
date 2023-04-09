from django.db import models

class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    company_id = models.IntegerField(max_length=500)
    device_name = models.CharField(max_length=100)
    device_description = models.CharField(max_length=200)
    

    class Meta:
        app_label = 'myapp'
        db_table = 'device'