from django.db import models


class Book(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, null=False)
    title = models.CharField(null=False, max_length=50)
    author = models.CharField(null=False, max_length=50)
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'Book {self.id}: {self.title}'

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author')
