from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.modelss.Company import Company
from myapp.serializers.serializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    @api_view(['POST'])
    def add_companies(request):
            serializer = CompanySerializer(data=request.data)
            if serializer.is_valid():
                company = serializer.save()
                return Response({'status': 'success', 'company_id': company.id}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    def update_companies(request, id):
        try:
            company = Company.objects.get(id=id)
            
        except Company.DoesNotExist:
            return Response({'status': 'error', 'message': 'Company does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def get_companies(request, id):
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist:
            return Response({'status': 'error', 'message': 'Company does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
