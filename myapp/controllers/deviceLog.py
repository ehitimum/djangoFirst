from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.modelss.Devicelog import Device_Log


@csrf_exempt

def add_device_logs(request, id, de_id):
    if request:
        data = request.POST
        company_id = id
        device_id = de_id
        employee_id = data.get('employee')
        checkout_time = data.get('checkout_time')
        return_time = data.get('return_time')
        checkout_condition = data.get('checkout_condition')
        return_condition = data.get('return_condition')

        if company_id:
            device_log = Device_Log(company_id=company_id, device_id=device_id, employee_id=employee_id, 
                                    checkout_time=checkout_time, return_time=return_time, 
                                    checkout_condition=checkout_condition, return_condition=return_condition)
            device_log.save()
            return JsonResponse({'status': 'Success'}, status=201)
        else:
            return JsonResponse({'status':'error'}, status=404)
    else:
        return JsonResponse({'status': 'error'}, status = 400)
#This one will show the logs of a device. There can be multiple logs for a device 
def show_device_log(request, id, de_id):
    if request:
        company_id = id
        device_id = de_id
       
        try:
            device_log = Device_Log.objects.filter(company_id= company_id, device_id = device_id)
            logs_data = []

            for i in device_log:
                data={
                    'id':i.id,
                    # 'device_id':i.device,
                    # 'employee_id':i.employee,
                    # 'company_id':i.company,
                    'checkout_time':i.checkout_time,
                    'return_time':i.return_time,
                    'checkout_condition':i.checkout_condition,
                    'return_condition':i.return_condition
                    
                }
                logs_data.append(data)
            return JsonResponse({'Logs': logs_data}, status=200)

        except Device_Log.DoesNotExist:
            return JsonResponse({'status':'error', 'message':'Employee does not exists in your company'}, status = 401)
        
    else:
        return JsonResponse({'status': 'error'}, status = 400)

#This ones job is to update some logs for information 
def update_device_logs(request, id, de_id, log_id):
    if request:
        data = request.POST
        company_id = id
        device_id = de_id
        log_id = log_id
        employee_id = data.get('employee')
        checkout_time = data.get('checkout_time')
        return_time = data.get('return_time')
        checkout_condition = data.get('checkout_condition')
        return_condition = data.get('return_condition')
       
        try:
            device_log = Device_Log.objects.get(company_id=company_id, device_id=device_id, id=log_id)
            device_log.employee_id = employee_id
            device_log.checkout_time = checkout_time
            device_log.return_time = return_time
            device_log.checkout_condition = checkout_condition
            device_log.return_condition = return_condition
            device_log.save()
            return JsonResponse({'status':'success'}, status = 201)
        except Device_Log.DoesNotExist:
            return JsonResponse({'status':'error', 'message':'Employee does not exists in your company'}, status = 401)

    else:
        return JsonResponse({'status': 'error'}, status = 400)