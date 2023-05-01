from django.db import models
from user.models import User
from book.models import Book


class Purchase(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f'Purchase {self.id}: by {self.user.first_name} user {self.book.title} book'

    class Meta:
        db_table = 'purchase'
