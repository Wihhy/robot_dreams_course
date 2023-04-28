from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    first_name = models.CharField(null=False, max_length=50)
    last_name = models.CharField(null=False, max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f'User {self.id}: {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'user'

