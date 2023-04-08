from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import Company
# from myapp.models.compModel import Company
from myapp.models import Company
# from myapp.modelss.compModel import Company

@csrf_exempt
def add_person(request):
    if request.method == 'GET':
        data = request.GET
        print(data)
        company = Company(company_name=data['company_name'], company_address=data['company_address'])
        company.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})