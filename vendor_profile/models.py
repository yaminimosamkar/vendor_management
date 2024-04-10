from django.db import models
from django.utils.translation import gettext as _
# from django.contrib.postgres.fields import JSONField

# Create your models here.

# Model to Add Vendor Information

# Vendor Management Profile
class EmployeeInformation(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True , verbose_name = 'Employee Code')
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()


# Purchase Order:

class PurchaseOrder( models.Model):
    po_number = models.CharField(max_length=50, unique=True , verbose_name = 'Purchase Order')
    vendor = models.ForeignKey("EmployeeInformation", verbose_name=_("Vendor Code"), on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField(auto_now=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status= models.CharField(max_length=50)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField(auto_now = True)
    acknowledgment_date = models.DateTimeField(auto_now=True)


class PerformanceReview(models.Model):
    vendor =  models.ForeignKey("EmployeeInformation", verbose_name=_("Vendor Performance Code"), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    



