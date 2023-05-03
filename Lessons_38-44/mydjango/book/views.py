from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Book


class AllBookView(ListView):
    model = Book


class BookView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = 'title', 'author', 'year', 'price'
    success_url = reverse_lazy('book-list')
    template_name = 'book/book_create.html'
