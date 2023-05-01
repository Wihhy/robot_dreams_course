from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy

from .models import Purchase
from django.views.generic import ListView, DetailView, CreateView


class AllPurchaseView(ListView):
    model = Purchase


class PurchaseView(DetailView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    fields = 'user', 'book'
    success_url = reverse_lazy('purchase-list')
    template_name = 'purchase/purchase_create.html'
