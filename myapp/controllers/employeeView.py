from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def add_employee(request):
    if request.method == 'GET':
        data = request.GET

        employee_name = data.get('employee_name')
        employee_title = data.get('employee_title')
        emloyee_coninfo = data.get('employee_coninfo')
    
    
    else:
        return JsonResponse({'status': 'error'}, status = 400)