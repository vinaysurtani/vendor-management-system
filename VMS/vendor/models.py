from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=30)
    contact_details = models.TextField(max_length=15)
    address = models.TextField(max_length=50)
    vendor_code = models.CharField(max_length=10, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.vendor_code + self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=10, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    STATUS_CHOICES = {
        "P" : "Pending",
        "C" : "Completed",
        "X" : "Cancelled",
    }
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    QUALITY_RATING_CHOICES = {
        1.0 : "ONE",
        2.0 : "TWO",
        3.0 : "THREE",
        4.0 : "FOUR",
        5.0 : "FIVE",
    }
    quality_rating = models.FloatField(default=0.0,blank=True,null=True,choices=QUALITY_RATING_CHOICES)
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.vendor.vendor_code + '-' + str(self.date)