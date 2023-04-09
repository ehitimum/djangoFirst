from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from myapp.modelss.Company import Company

# @csrf_exempt
# # This is add company funtion
# def add_companies(request):
#     #I am using postman to send a get request with json componenets
#     if request:
#         data = request.POST
#         #json components are below, The company_id is auto incremented
#         company_name = data.get('company_name')
#         company_address = data.get('company_address')
        
#         #if company name already exists in the database it will prevent in regestaring comapny name
        
        
#         company = Company(company_name=company_name, company_address=company_address)
#         company.save()
#         return JsonResponse({'status': 'success',
#                              'company_id':company.id}, status = 201)
#     else:
#         return JsonResponse({'status': 'error'}, status = 400)

# #This is for updating the company information such as name and address
# def update_companies(request, id):
#     if request:
#         data = request.POST
#         company_id = id
#         company_name = data.get('company_name')
#         company_address = data.get('company_address')
        
#         try:
#             company = Company.objects.get(id = company_id)
#         except Company.DoesNotExist:
#             return JsonResponse({'status':'error', 'message':'Company does not exists'}, status = 401)
#         company.company_name = company_name
#         company.company_address = company_address
#         company.save()
#         return JsonResponse({'status':'success'}, status = 201)
#     else:
#         return JsonResponse({'status':'error'}, status = 400)

# #This is for pulling the company information from the database through the comapny id
# def get_companies(request, id):
#     if request:
#         company_id = id
#         if company_id:
#             try:    
                
#                 company = Company.objects.get(id = company_id)
#                 return JsonResponse({
#                     'company_name':company.company_name,
#                     'company_address': company.company_address,
#                     'company_id': company.id
#                 })
#             except:
#                 return JsonResponse({
#                     'status':'error',
#                     'message':'Company information cannot be retrive due to company id and the request id is not matching.'
#                 },status = 401)
#         else:
#             return JsonResponse({'status':'error',
#                                  'message':'Missing Company_id'},status = 404)
#     else:
#         return JsonResponse({'status':'error'},status = 400)



from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.modelss.Company import Company
# from myapp.serializers import CompanySerializer
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    # serializer_class = CompanySerializer
    @api_view(['POST'])
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
                                'company_id':company.id}, status = 201)
        else:
            return JsonResponse({'status': 'error'}, status = 400)

    # @api_view(['PUT'])
    # def update_companies(request, id):
    #     try:
    #         company = Company.objects.get(id=id)
    #     except Company.DoesNotExist:
    #         return Response({'status': 'error', 'message': 'Company does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = CompanySerializer(company, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status': 'success'}, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['GET'])
    # def get_companies(request, id):
    #     try:
    #         company = Company.objects.get(id=id)
    #     except Company.DoesNotExist:
    #         return Response({'status': 'error', 'message': 'Company does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = CompanySerializer(company)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
