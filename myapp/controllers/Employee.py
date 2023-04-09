from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.modelss.Employee import Employee


@csrf_exempt

def add_employee(request):
    if request.method == 'POST':
        data = request.POST
        company_id = data.get('company_id', None)
        employee_name = data.get('employee_name')
        employee_title = data.get('employee_title')
        emloyee_contact_info = data.get('employee_contact_info')

        if company_id:
            employee = Employee(company_id=company_id, employee_name=employee_name, employee_title=employee_title,
                                 employee_contact_info=emloyee_contact_info)
            employee.save()
            return JsonResponse({'status: Success'}, status=201)
        else:
            return JsonResponse({'status':'error'}, status=404)
    else:
        return JsonResponse({'status': 'error'}, status = 400)