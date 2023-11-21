from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name = "Hot Dog",
            cooking_time = "5",
            ingredients = "Hot Dog Bun, Sausage, Ketchup, "+ 
            "Mayonnaise, Roasted Onions",
            ingredient_quantities = ((100, 'gram'), (50, 'gram'),\
                                      (20, 'milliliter'), (20, 'milliliter'), \
                                        (10, 'gram')),
            difficulty = "Intermediate",
            creator_id = 212
        )

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')

    def test_recipe_cooking_time(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('cooking_time').verbose_name

        self.assertEqual(field_label, 'cooking time')

    def test_recipe_ingredients(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('ingredients').verbose_name

        self.assertEqual(field_label, 'ingredients')

    def test_recipe_ingredients(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('ingredient_quantities').verbose_name

        self.assertEqual(field_label, 'ingredient quantities')

    def test_recipe_difficulty(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('difficulty').verbose_name

        self.assertEqual(field_label, 'difficulty')

    def test_recipe_creator_id(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('creator_id').verbose_name

        self.assertEqual(field_label, 'creator id')