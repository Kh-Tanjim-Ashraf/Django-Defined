from rest_framework import serializers
from employee.models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    # Since it's a foreign key, this invokes the target model 'Company' to display a human-readable name instead of DB id.
    company = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ["name", "phone", "company"]