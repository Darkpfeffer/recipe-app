from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import User
from recipes.models import Recipe
from ingredients.models import Ingredient

# Create your tests here.
class UserModelTest(TestCase):
    def setUpTestData():
        user= get_user_model().objects.create_user(
            username = 'testuser', password='secret'
        )
        
        test_user = User.objects.create(
            user_info = user
        )

        test_ingredient = Ingredient.objects.create(
            name = "salt",
            price = 0.50,
            ingredient_unit_type = "kilogram"
        )

        test_recipe1 = Recipe.objects.create(
            name = 'Test recipe',
            cooking_time = 5,
            difficulty = "Intermediate",
            creator = test_user
        )

        test_recipe2 =Recipe.objects.create(
            name = 'Test recipe2',
            cooking_time = 5,
            difficulty = "Intermediate",
            creator = test_user
        )

        test_recipe1.ingredients.add(test_ingredient)

        test_recipe2.ingredients.add(test_ingredient)

        test_user.favorite_recipes.add(test_recipe1, test_recipe2)

    def test_user_username(self):
        user = User.objects.get(id = 1)

        field_label = user._meta.get_field('user_info').verbose_name

        self.assertEqual(field_label, 'user info')

    def test_user_favorite_recipes(self):
        user = User.objects.get(id = 1)

        field_label = user._meta.get_field('favorite_recipes').verbose_name

        self.assertEqual(field_label, 'favorite recipes')

    def test_user_profile_pic(self):
        user = User.objects.get(id = 1)

        field_label = user._meta.get_field('profile_pic').verbose_name

        self.assertEqual(field_label, 'profile pic')