from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.modelss.Device import Device


@csrf_exempt

def add_devices(request, id):
    if request:
        data = request.POST
        company_id = id
        device_name = data.get('device_name')
        device_description = data.get('device_description')
       
       

        if company_id:
            device = Device(company_id=company_id, device_name=device_name, device_description=device_description)
            device.save()
            return JsonResponse({'status': 'Success'}, status=201)
        else:
            return JsonResponse({'status':'error'}, status=404)
    else:
        return JsonResponse({'status': 'error'}, status = 400)
    
def update_device_info(request, id, de_id):
    if request:
        data = request.POST
        company_id = id
        device_id = de_id
        device_name = data.get('device_name')
        device_description = data.get('device_description')
       
        try:
            device = Device.objects.get(company_id= company_id, id=device_id)
            device.device_name = device_name
            device.device_description = device_description
            device.save()
            return JsonResponse({'status':'success'}, status = 201)
        except Device.DoesNotExist:
            return JsonResponse({'status':'error', 'message':'Employee does not exists in your company'}, status = 401)

    else:
        return JsonResponse({'status': 'error'}, status = 400)

def show_employees(request, id):
    if request:
        company_id = id
       
        try:
            device = Device.objects.filter(company_id= company_id)
            devices_data = []

            for i in device:
                device_data={
                    'id':i.id,
                    'device_name':i.device_name,
                    'device_description':i.device_description
                    
                }
                devices_data.append(device_data)
            return JsonResponse({'Device': devices_data}, status=200)

        except Device.DoesNotExist:
            return JsonResponse({'status':'error', 'message':'Employee does not exists in your company'}, status = 401)
        
    else:
        return JsonResponse({'status': 'error'}, status = 400)