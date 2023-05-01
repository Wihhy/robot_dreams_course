from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', BookView.as_view(), name='book-detail'),
    path('all/', AllBookView.as_view(), name='book-list'),
    path('create/', BookCreateView.as_view(), name='book-create')

]
