from django.shortcuts import render
from django.http import JsonResponse
from .models import Purchase


def all_purchases(request):
    data = Purchase.objects.all().values()
    return JsonResponse(list(data), safe=False)

