from django.urls import path
from .views import *

urlpatterns = [
    path('all/', all_purchases, name='all_purchases')
]