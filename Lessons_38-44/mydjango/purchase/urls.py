from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', PurchaseView.as_view(), name='purchase-detail'),
    path('all/', AllPurchaseView.as_view(), name='purchase-list'),
    path('create/', PurchaseCreateView.as_view(), name='user-create')

]
