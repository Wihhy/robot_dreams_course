from celery import shared_task
from .models import User
from purchase.models import Purchase

@shared_task
def printer():
    print('I`m printer')


@shared_task
def purchase_counter(user_id):
    user = User.objects.get(id=user_id)
    purchase_count = Purchase.objects.filter(user=user).count()
    print(purchase_count)


@shared_task
def user_counter():
    print(User.objects.all().count())
