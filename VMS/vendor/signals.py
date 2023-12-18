from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver
from django.db.models import Avg,F,ExpressionWrapper,DurationField
from django.utils import timezone
from django.db import transaction

@receiver(post_save,sender=PurchaseOrder)
def performance_tab(sender,instance,**kwargs):
    vendor = instance.vendor
    completed_purchase_orders = PurchaseOrder.objects.filter(vendor=vendor,status='C')
    on_time_orders = completed_purchase_orders.filter(delivery_date__lte=instance.delivery_date)

    on_time_delivery_rate = (on_time_orders.count()/completed_purchase_orders.count()) * 100 if completed_purchase_orders.count() > 0 else 0.0

    quality_rate = PurchaseOrder.objects.filter(vendor=vendor,status='C',quality_rating__isnull=False).aggregate(quality_rating__avg=Avg('quality_rating'))

    quality_rating_avg= quality_rate.get('quality_rating__avg',0.0)
    if quality_rating_avg == None:
        quality_rating_avg=0.0


    ack_purchase_orders = PurchaseOrder.objects.filter(vendor=vendor,acknowledgement_date__isnull=False)

    response_time = ack_purchase_orders.aggregate(response_time_avg=Avg(ExpressionWrapper(F('acknowledgement_date') - F('issue_date'),output_field=DurationField())))

    average_response_time = response_time.get('response_time_avg',0.0)
    if average_response_time.total_seconds() < 0:
        average_response_time =0.0

    issued_purchase_orders = PurchaseOrder.objects.filter(vendor=vendor)
    fulfillment_rate = (completed_purchase_orders.count()/issued_purchase_orders.count()) * 100 if issued_purchase_orders.count() > 0 else 0.0

    vendor.on_time_delivery_rate=on_time_delivery_rate
    vendor.quality_rating_avg=quality_rating_avg
    vendor.average_response_time=round(average_response_time.total_seconds() if average_response_time else 0.0,2)
    vendor.fulfillment_rate=fulfillment_rate
    vendor.save()

    with transaction.atomic():
        historical_performance = HistoricalPerformance.objects.create(
            vendor=vendor,
            date=timezone.now(),
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=round(average_response_time.total_seconds() if average_response_time else 0.0,2),
            fulfillment_rate=fulfillment_rate,
        )
