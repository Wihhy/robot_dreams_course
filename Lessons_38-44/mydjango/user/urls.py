from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('<int:pk>', UserView.as_view(), name='user-detail'),
    path('all/', AllUserView.as_view(), name='user-list'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('celery/', celery, name='celery-view')
]

router = DefaultRouter()
router.register('viewset', UserViewSet, basename='user-view-set')
urlpatterns += router.urls
