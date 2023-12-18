from django.urls import path,include
from vendor import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.api_root),
    path('vendors/',views.VendorList.as_view(),name='vendors-list-create'),
    path('vendors/<str:vendor_code>/',views.VendorDetail.as_view()),
    path('vendors/<int:vendor>/performance/',views.HistoricalPerformanceList.as_view()),
    path('purchase-orders/',views.PurchaseOrderList.as_view(),name='purchase-orders-list-create'),
    path('purchase-orders/<str:po_number>/',views.PurchaseOrderDetail.as_view()),
    path('purchase-orders/<str:po_number>/acknowledge',views.AcknowledgeUpdate.as_view()),
    path('apitoken/', obtain_auth_token),
]