# import json
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Person

# def say_hello(request):
#     return HttpResponse('Hello World')




# @csrf_exempt
# def add_person(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             # person = Person(name=data['name'], age=data['age'])
#             # person.save()
#             return JsonResponse({'status': 'success'})
#         except:
#             return JsonResponse({'status': 'error1'})
#     else:
#         return JsonResponse({'status': 'error2'})



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .models import Company
from myapp.models import Company
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