from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        from myapp.modelss.Company import Company
        from myapp.modelss.Employee import Employee
        from myapp.modelss.Device import Device
        from myapp.modelss.Devicelog import Device_Log
        


