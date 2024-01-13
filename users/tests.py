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
        
        User.objects.create(
            username = user,
            name = "Erik Vasquez",
            email = "vasquez@example.com",
            birthday = "1212-12-12",
            profile_pic = 'no_picture.jpg'
        )

        user_object = User.objects.get(id=1)

        Ingredient.objects.create(
            name = "salt",
            price = 0.50,
            ingredient_unit_type = "kilogram"
        )

        Recipe.objects.create(
            name = 'Test recipe',
            cooking_time = 5,
            ingredient_quantities = ((100, 'gram'), (50, 'gram'), 
                                     (20, 'milliliter')),
            difficulty = "Intermediate",
            creator_id = user_object
        )

        Recipe.objects.create(
            name = 'Test recipe2',
            cooking_time = 5,
            ingredient_quantities = ((100, 'gram'), (50, 'gram'), 
                                     (20, 'milliliter')),
            difficulty = "Intermediate",
            creator_id = user_object
        )

        ingredient_object_query = Ingredient.objects.filter(id=1)

        recipe_object = Recipe.objects.get(id=1)

        recipe_object2 = Recipe.objects.get(id=2)

        recipe_object.ingredients.set(ingredient_object_query)

        recipe_object2.ingredients.set(ingredient_object_query)

        user_object.favorite_recipes.add(recipe_object, recipe_object2)

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

    def test_user_profile_pic(self):
        user = User.objects.get(id = 1)

        field_label = user._meta.get_field('profile_pic').verbose_name

        self.assertEqual(field_label, 'profile pic')