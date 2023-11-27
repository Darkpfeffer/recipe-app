from django.test import TestCase
from .models import Ingredient
from django.contrib.auth import get_user_model
from recipes.models import Recipe
from users.models import User

# Create your tests here.

class IngredientModelTest(TestCase):
    def setUpTestData():
        Ingredient.objects.create(
            name = "salt",
            supplier = "Someone",
            price = 0.50,
            ingredient_unit_type = "kilogram"
        )

        user= get_user_model().objects.create_user(
            username = 'testuser', password='secret'
        )

        User.objects.create(
            username = user,
            name = "Erik Vasquez",
            email = "vasquez@example.com",
            birthday = "1212-12-12"
        )

        test_user = User.objects.get(id=1)

        test_ingredient_query = Ingredient.objects.filter(id=1)

        test_ingredient = Ingredient.objects.get(id=1)
        
        Recipe.objects.create(
            name = "Hot Dog",
            cooking_time = "5",
            ingredient_quantities = ((100, 'gram'), (50, 'gram'),\
                                      (20, 'milliliter'), (20, 'milliliter'), \
                                        (10, 'gram')),
            difficulty = "Intermediate",
            creator_id = test_user
        )

        test_recipe = Recipe.objects.get(id=1)

        test_recipe.ingredients.set(test_ingredient_query)

        test_recipe.save()

        test_ingredient.recipe_appearance.add(test_recipe)

        test_ingredient.save()

    def test_ingredient_name(self):
        ingredient = Ingredient.objects.get(id = 1)

        field_label = ingredient._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')

    def test_ingredient_supplier(self):
        ingredient = Ingredient.objects.get(id = 1)

        field_label = ingredient._meta.get_field('supplier').verbose_name

        self.assertEqual(field_label, 'supplier')

    def test_ingredient_price(self):
        ingredient = Ingredient.objects.get(id = 1)

        field_label = ingredient._meta.get_field('price').verbose_name

        self.assertEqual(field_label, 'price')

    def test_ingredient_ingredients_unit_type(self):
        ingredient = Ingredient.objects.get(id = 1)

        field_label = ingredient._meta.get_field('ingredient_unit_type').verbose_name

        self.assertEqual(field_label, 'ingredient unit type')

    def test_ingredient_recipe_appearance(self):
        ingredient = Ingredient.objects.get(id = 1)

        field_label = ingredient._meta.get_field('recipe_appearance').verbose_name

        self.assertEqual(field_label, 'recipe appearance')