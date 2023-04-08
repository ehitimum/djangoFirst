from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=200)

    class Meta:
        app_label = 'myapp'
        db_table = 'company'