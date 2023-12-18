from django.shortcuts import render
from rest_framework import generics,status
from .serializers import VendorSerializer,HistoricalPerformanceSerializer, PurchaseOrderSerializer,AckSerializer
from .models import *
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication

# Create your views here.

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'vendors': reverse('vendors-list-create',request=request,format=format),
        'purchase-orders' : reverse('purchase-orders-list-create',request=request,format=format)
    })

class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'vendor_code'

    def get_queryset(self):
        self.pk = self.kwargs['vendor_code']
        return Vendor.objects.filter(vendor_code = self.pk)

class PurchaseOrderList(generics.ListCreateAPIView):
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        vendor = self.request.query_params.get('vendor')
        if vendor is not None:
            queryset = queryset.filter(vendor=vendor)
        return queryset

class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'po_number'
    
    def get_queryset(self):
        self.pk = self.kwargs['po_number']
        return PurchaseOrder.objects.filter(po_number = self.pk)

class HistoricalPerformanceList(generics.ListAPIView):
    
    serializer_class = HistoricalPerformanceSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.pk = self.kwargs['vendor']
        return HistoricalPerformance.objects.filter(vendor = self.pk)

class AcknowledgeUpdate(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = AckSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.validated_data['acknowledgement_date']=timezone.now()
        super().perform_update(serializer)
        return Response(serializer.data)