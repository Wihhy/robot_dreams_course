from django.shortcuts import render
from django.http import JsonResponse
from .models import Book


def all_books(request):
    data = Book.objects.all().values()
    return JsonResponse(list(data), safe=False)
