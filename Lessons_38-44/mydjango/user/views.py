from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import User


class AllUserView(ListView):
    model = User


class UserView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    # form_class = UserForm
    fields = 'first_name', 'last_name', 'age'
    success_url = reverse_lazy('user-list')
    template_name = 'user/user_create.html'
