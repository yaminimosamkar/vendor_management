from rest_framework import serializers
from .models import *

class EmployeeInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInformation
        fields = ['name', 'contact_details', 'address', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']