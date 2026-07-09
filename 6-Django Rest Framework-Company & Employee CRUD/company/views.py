from rest_framework.views import APIView
from company.models import Company
from company.serializer import CompanySerializer
from rest_framework.response import Response
from rest_framework import status



class CompanyView(APIView):

    def get(self, request):
        companies = Company.objects.all()
        serialized = CompanySerializer(instance=companies, many=True)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serialized = CompanySerializer(data=request.data)
        
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



class CompanyDetailView(APIView):

    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        serialized = CompanySerializer(instance=company)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        company = Company.objects.get(pk=pk)
        serialized = CompanySerializer(instance=company, data=request.data)
        
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        company = Company.objects.get(pk=pk)
        serialized = CompanySerializer(instance=company, data=request.data, partial=True)
        
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)