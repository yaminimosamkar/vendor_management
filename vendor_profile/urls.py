from django.urls import path
from . import views

urlpatterns = [
    # path('test/', views.test , name='test-page'),
    # path('home/', views.add , name='add-page'),


    path('vendors/' ,views.add_vendor, name = 'vendors-page'),
    path('vendors/<int:vendor_id>/' , views.get_vendor_information),
    path('vendors/<int:vendor_id>', views.delete_vendor_details)
]
