from django.db import models

class Device_Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    device_id = models.IntegerField(max_length=500)
    employee_id = models.IntegerField(max_length=500)
    company_id = models.IntegerField(max_length=500)
    checkout_time = models.DateTimeField()
    return_time = models.DateTimeField()
    checkout_condition = models.CharField(max_length=100)
    return_condition = models.CharField(max_length=200)
    

    class Meta:
        app_label = 'myapp'
        db_table = 'device_log'