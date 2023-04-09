from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import Company
# from myapp.models.compModel import Company
# from myapp.models import Company
from myapp.modelss.compModel import Company

@csrf_exempt
# This is add company funtion
def add_company(request):
    #I am using postman to send a get request with json componenets
    if request.method == 'GET':
        data = request.GET
        #json components are below, The company_id is auto incremented
        company_name = data.get('company_name')
        company_address = data.get('company_address')
        
        #if company name already exists in the database it will prevent in regestaring comapny name
        if Company.objects.filter(company_name=company_name).exists():
            return JsonResponse({'status': 'error', 'message': 'Company already exists'}, status = 404)
        
        company = Company(company_name=company_name, company_address=company_address)
        company.save()
        return JsonResponse({'status': 'success',
                             'company_id':company.company_id}, status = 201)
    else:
        return JsonResponse({'status': 'error'}, status = 400)

#This is for updating the company information such as name and address
def update_company(request):
    if request.method == 'GET':
        data = request.GET
        #here by default if anyone changes any information like company name, address database will update,
        #if they changes one field frontend actually send both field but only one of them gets updated while other one remains same.
        #company_id I am assuming hidden and any sord of request it will also be send along.
        
        company_id = data.get('company_id')
        company_name = data.get('company_name')
        company_address = data.get('company_address')
        
        try:
            #if id matches the company_id in the database then the only the field that is updated will be changed.
            company = Company.objects.get(company_id = company_id)
        except Company.DoesNotExist:
            return JsonResponse({'status':'error', 'message':'Company does not exists'}, status = 401)
        company.company_name = company_name
        company.company_address = company_address
        company.save()
        return JsonResponse({'status':'success'}, status = 201)
    else:
        return JsonResponse({'status':'error'}, status = 400)

#This is for pulling the company information from the database through the comapny id
def get_company(request):
    if request.method == 'GET':
        data = request.GET
        company_id = data.get('company_id', None)

        #if Id doesnt send via request api, then the process wont start

        if company_id:
            try:    
                #if id matches the company_id in the database then the information will be provided
                company = Company.objects.get(company_id = company_id)
                return JsonResponse({
                    'company_name':company.company_name,
                    'company_address': company.company_address,
                    'company_id': company.company_id
                })
            except:
                return JsonResponse({
                    'status':'error',
                    'message':'Company information cannot be retrive due to company id and the request id is not matching.'
                },status = 401)
        else:
            return JsonResponse({'status':'error',
                                 'message':'Missing Company_id'},status = 404)
    else:
        return JsonResponse({'status':'error'},status = 400)