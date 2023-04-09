from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import Company
# from myapp.models.compModel import Company
# from myapp.models import Company
from myapp.modelss.compModel import Company

@csrf_exempt
def add_company(request):
    if request.method == 'GET':
        data = request.GET
        company_name = data.get('company_name')
        company_address = data.get('company_address')
        
        if Company.objects.filter(company_name=company_name).exists():
            return JsonResponse({'status': 'error', 'message': 'Company already exists'})
        
        company = Company(company_name=company_name, company_address=company_address)
        company.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})




# def add_company(request):
#     if request.method == 'GET':
#         data = request.GET
#         print(data)
#         company = Company(company_name=data['company_name'], company_address=data['company_address'])
#         company.save()
#         return JsonResponse({'status': 'success'})
#     else:
#         return JsonResponse({'status': 'error'})
    
def update_company(request):
    if request.method == 'GET':
        data = request.GET
        company_id = data.get('company_id')
        company_name = data.get('company_name')
        company_address = data.get('company_address')
        
        try:
            company = Company.objects.get(company_id = company_id)
        except Company.DoesNotExist:
            return JsonResponse({'status':'error', 'message':'Company does not exists'})
        company.company_name = company_name
        company.company_address = company_address
        company.save()
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'error'})

def get_company(request):
    if request.method == 'GET':
        data = request.GET
        company_id = data.get('company_id', None)
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
                })
        else:
            return JsonResponse({'status':'error',
                                 'message':'Missing Company_id'})
    else:
        return JsonResponse({'status':'error'})