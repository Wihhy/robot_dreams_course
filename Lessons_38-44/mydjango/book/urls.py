from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('<int:pk>', BookView.as_view(), name='book-detail'),
    path('all/', AllBookView.as_view(), name='book-list'),
    path('create/', BookCreateView.as_view(), name='book-create')
]

router = DefaultRouter()
router.register('viewset', BookViewSet, basename='book-view-set')
urlpatterns += router.urls
