from django.urls import path
from .views import *

urlpatterns = [
    path('', users, name='users'),
    path('all/', all_users, name='all_users')
]