from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class AllUserView(ListView):
    model = User


class UserView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = 'first_name', 'last_name', 'age'
    success_url = reverse_lazy('user-list')
    template_name = 'user/user_create.html'


class UserPagination(PageNumberPagination):
    page_size = 10


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filterset_fields = ['first_name', 'last_name', 'age']
    ordering_fields = ['first_name', 'last_name', 'age']
