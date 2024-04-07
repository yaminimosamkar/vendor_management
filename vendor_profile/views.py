from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeInformationSerializer

# Create your views here.
def test(request):
    return render( request, 'test.html')

# @api_view(['POST'])
# def add_vendor(request):
#     if request.method == 'POST':
