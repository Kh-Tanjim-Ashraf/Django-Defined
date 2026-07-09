from rest_framework.views import APIView
from rest_framework.response import Response
from employee.models import Employee
from employee.serializer import EmployeeSerializer
from rest_framework import status



class EmployeeView(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serialized = EmployeeSerializer(instance=employees, many=True)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serialized = EmployeeSerializer(data=request.data)
        
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



class EmployeeDetailView(APIView):

    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serialized = EmployeeSerializer(instance=employee)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serialized = EmployeeSerializer(instance=employee, data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serialized = EmployeeSerializer(instance=employee, data=request.data, partial=True)

        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)