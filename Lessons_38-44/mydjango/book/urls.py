from django.urls import path
from .views import *

urlpatterns = [
    path('all/', all_books, name='all_books')
]
