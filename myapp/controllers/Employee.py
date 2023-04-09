from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from myapp.modelss.Company import Company

from myapp.modelss.Employee import Employee
from myapp.serializers.serializer import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    @api_view(['POST'])
    
    def add_employees(request):
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                employee = serializer.save()
                return Response({'status': 'success', 'employee_id': employee.id}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def add_employees(request, id):
    #     if request:
    #         data = request.POST
    #         company_id = id
    #         employee_name = data.get('employee_name')
    #         employee_title = data.get('employee_title')
    #         employee_contact_info= data.get('employee_contact_info')
       

    #         if company_id:
    #             employee = Employee(company_id=company_id, employee_name=employee_name, employee_title=employee_title,
    #                                 employee_contact_info=employee_contact_info)
    #             employee.save()
    #             return Response({'status': 'Success'}, status=201)
    #         else:
    #             return Response({'status':'error'}, status=404)
    #     else:
    #         return Response({'status': 'error'}, status = 400)





       
    
# def update_employees(request, id, emp_id):
#     if request:
#         data = request.POST
#         company_id = id
#         employee_id = emp_id
#         employee_name = data.get('employee_name')
#         employee_title = data.get('employee_title')
#         employee_contact_info= data.get('employee_contact_info')
       
#         try:
#             employee = Employee.objects.get(company_id= company_id, id=employee_id)
#             employee.employee_name = employee_name
#             employee.employee_title = employee_title
#             employee.employee_contact_info = employee_contact_info
#             employee.save()
#             return JsonResponse({'status':'success'}, status = 201)
#         except Employee.DoesNotExist:
#             return JsonResponse({'status':'error', 'message':'Employee does not exists in your company'}, status = 401)

#     else:
#         return JsonResponse({'status': 'error'}, status = 400)
    


# def show_employees(request, id):
#     if request:
#         company_id = id
       
#         try:
#             employee = Employee.objects.filter(company_id= company_id)
#             employees_data = []

#             for i in employee:
#                 employee_data={
#                     'employee_id':i.id,
#                     'employee_name':i.employee_name,
#                     'employee_title':i.employee_title,
#                     'employee_contact_info':i.employee_contact_info
#                 }
#                 employees_data.append(employee_data)
#             return JsonResponse({'employees': employees_data}, status=200)

#         except Employee.DoesNotExist:
#             return JsonResponse({'status':'error', 'message':'Employee does not exists in your company'}, status = 401)
        
#     else:
#         return JsonResponse({'status': 'error'}, status = 400)
    

# def get_employee_info(request, id, emp_id):
#     if request:
#         data = request.POST
#         company_id = id
#         employee_id = emp_id
#         employee_name = data.get('employee_name')
#         employee_title = data.get('employee_title')
#         employee_contact_info= data.get('employee_contact_info')
       
#         try:
#             employee = Employee.objects.get(company_id= company_id, id=employee_id)
            
#             return JsonResponse({'employee_id':employee_id,
#                                  'employee_name':employee_name,
#                                  'employee_title':employee_title,
#                                  'employee_contact_info':employee_contact_info}, status = 201)
#         except Employee.DoesNotExist:
#             return JsonResponse({'status':'error', 'message':'Employee does not exists in your company'}, status = 401)

#     else:
#         return JsonResponse({'status': 'error'}, status = 400)