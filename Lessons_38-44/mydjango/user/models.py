from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    first_name = models.CharField(null=False, max_length=50)
    last_name = models.CharField(null=False, max_length=50)
    age = models.IntegerField()

    class Meta:
        db_table = 'user'




