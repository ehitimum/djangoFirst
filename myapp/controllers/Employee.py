from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.modelss.Employee import Employee


@csrf_exempt

def add_employees(request, id):
    if request:
        data = request.POST
        company_id = id
        employee_name = data.get('employee_name')
        employee_title = data.get('employee_title')
        employee_contact_info= data.get('employee_contact_info')
       

        if company_id:
            employee = Employee(company_id=company_id, employee_name=employee_name, employee_title=employee_title,
                                 employee_contact_info=employee_contact_info)
            employee.save()
            return JsonResponse({'status': 'Success'}, status=201)
        else:
            return JsonResponse({'status':'error'}, status=404)
    else:
        return JsonResponse({'status': 'error'}, status = 400)
#update an eployee information
def update_employees(request, id, emp_id):
    if request:
        data = request.POST
        company_id = id
        employee_id = emp_id
        employee_name = data.get('employee_name')
        employee_title = data.get('employee_title')
        employee_contact_info= data.get('employee_contact_info')
       
        try:
            employee = Employee.objects.get(company_id= company_id, id=employee_id)
            employee.employee_name = employee_name
            employee.employee_title = employee_title
            employee.employee_contact_info = employee_contact_info
            employee.save()
            return JsonResponse({'status':'success'}, status = 201)
        except Employee.DoesNotExist:
            return JsonResponse({'status':'error', 'message':'Employee does not exists in your company'}, status = 401)

    else:
        return JsonResponse({'status': 'error'}, status = 400)
    

#Show all the employee list under a company
def show_employees(request, id):
    if request:
        company_id = id
       
        try:
            employee = Employee.objects.filter(company_id= company_id)
            employees_data = []

            for i in employee:
                employee_data={
                    'employee_id':i.id,
                    'employee_name':i.employee_name,
                    'employee_title':i.employee_title,
                    'employee_contact_info':i.employee_contact_info,
                }
                employees_data.append(employee_data)
            return JsonResponse({'employees': employees_data}, status=200)

        except Employee.DoesNotExist:
            return JsonResponse({'status':'error', 'message':'Employee does not exists in your company'}, status = 401)
        
    else:
        return JsonResponse({'status': 'error'}, status = 400)
    

def get_employee_info(request, id, emp_id):
    if request:
        data = request.POST
        company_id = id
        employee_id = emp_id
        employee_name = data.get('employee_name')
        employee_title = data.get('employee_title')
        employee_contact_info= data.get('employee_contact_info')
       
        try:
            employee = Employee.objects.get(company_id= company_id, id=employee_id)
            
            return JsonResponse({'employee_id':employee_id,
                                 'employee_name':employee_name,
                                 'employee_title':employee_title,
                                 'employee_contact_info':employee_contact_info}, status = 201)
        except Employee.DoesNotExist:
            return JsonResponse({'status':'error', 'message':'Employee does not exists in your company'}, status = 401)

    else:
        return JsonResponse({'status': 'error'}, status = 400)