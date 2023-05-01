from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', UserView.as_view(), name='user-detail'),
    path('all/', AllUserView.as_view(), name='user-list'),
    path('create/', UserCreateView.as_view(), name='user-create')
]
