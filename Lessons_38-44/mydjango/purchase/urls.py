from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('<int:pk>', PurchaseView.as_view(), name='purchase-detail'),
    path('all/', AllPurchaseView.as_view(), name='purchase-list'),
    path('create/', PurchaseCreateView.as_view(), name='user-create')

]

router = DefaultRouter()
router.register('viewset', PurchaseViewSet, basename='purchase-view-set')
urlpatterns += router.urls
