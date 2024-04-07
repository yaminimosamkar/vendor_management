from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

# Model to Add Vendor Information
class EmployeeInformation(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True , verbose_name = 'Employee Code')
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()