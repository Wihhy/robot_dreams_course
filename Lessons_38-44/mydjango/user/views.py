from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User


def users(request):
    return HttpResponse('Hello, users!')


def all_users(request):
    data = User.objects.all().values()
    return JsonResponse(list(data), safe=False)
