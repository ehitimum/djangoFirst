from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.modelss.Company import Company

@csrf_exempt
# This is add company funtion
def add_companies(request):
    #I am using postman to send a get request with json componenets
    if request:
        data = request.POST
        #json components are below, The company_id is auto incremented
        company_name = data.get('company_name')
        company_address = data.get('company_address')
        
        #if company name already exists in the database it will prevent in regestaring comapny name
        
        
        company = Company(company_name=company_name, company_address=company_address)
        company.save()
        return JsonResponse({'status': 'success',
                             'company_id':company.company_id}, status = 201)
    else:
        return JsonResponse({'status': 'error'}, status = 400)

#This is for updating the company information such as name and address
def update_companies(request, id):
    if request:
        data = request.POST
        company_id = id
        company_name = data.get('company_name')
        company_address = data.get('company_address')
        
        try:
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
def get_companies(request, id):
    if request:
        company_id = id
        if company_id:
            try:    
                
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