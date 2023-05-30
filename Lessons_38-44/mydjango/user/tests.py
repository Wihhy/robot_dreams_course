from django.test import TestCase
import factory
import random
from .models import User


class RandomUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(1, 100)

    class Meta:
        model = User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()

    def test_create(self):
        self.assertIsInstance(self.user, User)


class UserViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()

    def test_users_list(self):
        resp = self.client.get(f'/viewset/')
        print(resp)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('count'), 1)
        random_number = random.randint(1, 10)
        for _ in range(random_number):
            RandomUserFactory.create()
        resp = self.client.get(f'/viewset/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('count'), random_number + 1)

    def test_get_user_detail(self):
        resp = self.client.get(f'/viewset/{self.user.id}/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('first_name'), self.user.first_name)

    def test_user_create(self):
        user_data = {
            'first_name': 'Created User',
            'age': 1
        }
        resp = self.client.post('/viewset/', data=user_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json().get('first_name'), user_data.get('first_name'))

    def test_user_delete(self):
        resp = self.client.delete(f'/viewset/{self.user.id}/')
        self.assertEqual(resp.status_code, 204)
