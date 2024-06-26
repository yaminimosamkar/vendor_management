from django.shortcuts import render
from rest_framework.response import Response
from vendor_profile.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions


@csrf_exempt
@api_view([ 'POST'])
@permission_classes((permissions.AllowAny,))
def add_vendor(request):
    # if request.method == 'GET':
    #     vendor_list = EmployeeInformation.objects.all()
    #     serializer = EmployeeInformationSerializer(vendor_list, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = EmployeeInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('serializer--------------------', serializer)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

@api_view(['GET', 'PUT'])
@permission_classes((permissions.AllowAny,))
def get_vendor_information(request, vendor_id):
    try:
        vendor_info = EmployeeInformation.objects.get(id=vendor_id)
    except EmployeeInformation.DoesNotExist:
        raise Http404("Vendor does not exist")

    if request.method == 'GET':
        serializer = EmployeeInformationSerializer(vendor_info)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeInformationSerializer(vendor_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def delete_vendor_details(request, vendor_id):
    try:
        vendor = EmployeeInformation.objects.get(id = vendor_id)
        print ('vendor******* delete_vendor_details' , vendor)
    except EmployeeInformation.DoesNotExist:
        raise Http404('Vendor Doe not Exists')

    if request.method == 'DELETE':
        vendor.delete()
        return JsonResponse({'message' : 'Vendor Deleted Successfully'} , status = 204)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# Function to Add the Purchase order and get the list of Purchase order
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_create_purchase_order(request):
    if request.method == 'GET':
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:
        return Response({'error': 'Method Not Allowed'}, status=405)


# Function to get the Purchase Order according to the Purchase or ID and Update it 

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def update_get_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
        print ('purchase_order-------update_get_purchase_order' , purchase_order)
    except PurchaseOrder.DoesNotExist:
        raise Http404("Purchase Order does not exist")

    if request.method == 'GET':
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        purchase_order.delete()
        return JsonResponse({'message': 'Purchase Order Deleted Successfully'}, status=204)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

# Delete the data with specific ID

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def delete_purchase_order(request, po_id):
    try:
        purchase_data = PurchaseOrder.objects.get(id=po_id)
        print ( 'purchase_data ------ Delete ORder Details' , purchase_data)
    except PurchaseOrder.DoesNotExist:
        raise Http404('Vendor Doe not Exists')

    if request.method == 'DELETE':
        purchase_data.delete()
        return JsonResponse({'message' : 'Purchase Order Deleted Successfully'} , status = 204)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
# Review Performance Metrics:




    
