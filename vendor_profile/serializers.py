from rest_framework import serializers
from .models import *

class EmployeeInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInformation
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'