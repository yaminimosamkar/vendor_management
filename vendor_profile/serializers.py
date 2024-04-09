from rest_framework import serializers
from .models import EmployeeInformation

class EmployeeInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInformation
        fields = '__all__'