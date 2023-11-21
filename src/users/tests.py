from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import User

# Create your tests here.
class UserModelTest(TestCase):
    def setUpTestData():
        user= get_user_model().objects.create_user(
            username = 'testuser', password='secret'
        )

        User.objects.create(
            username = user,
            name = "Erik Vasquez",
            email = "vasquez@example.com",
            birthday = "1212-12-12",
            favorite_recipes = "1"
        )

    def test_user_username(self):
        user = User.objects.get(id = 1)

        field_label = user._meta.get_field('username').verbose_name

        self.assertEqual(field_label, 'username')

    def test_user_name(self):
        user = User.objects.get(id = 1)

        field_label = user._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')

    def test_user_email(self):
        user = User.objects.get(id = 1)

        field_label = user._meta.get_field('email').verbose_name

        self.assertEqual(field_label, 'email')

    def test_user_birthday(self):
        user = User.objects.get(id = 1)

        field_label = user._meta.get_field('birthday').verbose_name

        self.assertEqual(field_label, 'birthday')
        
    def test_user_favorite_recipes(self):
        user = User.objects.get(id = 1)

        field_label = user._meta.get_field('favorite_recipes').verbose_name

        self.assertEqual(field_label, 'favorite recipes')