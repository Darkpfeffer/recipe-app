from django.test import TestCase
from .models import Ingredient
from .forms import CreateIngredientForm
from django.contrib.auth import get_user_model
from recipes.models import Recipe
from users.models import User
import tempfile

# Create your tests here.

class IngredientModelTest(TestCase):
    def setUpTestData():
        test_ingredient = Ingredient.objects.create(
            name = "salt",
            price = 0.50,
            ingredient_unit_type = "kilogram",
            pic = 'no_picture.jpg'
        )

        user= get_user_model().objects.create_user(
            username = 'testuser', password='secret'
        )

        test_user = User.objects.create(
            user_info = user
        )

        test_user = User.objects.get(id=1)
        
        Recipe.objects.create(
            name = "Hot Dog",
            cooking_time = "5",
            difficulty = "Intermediate",
            creator = test_user
        )

        test_recipe = Recipe.objects.get(id=1)

        test_ingredient.recipe_appearance.add(test_recipe)

    def test_ingredient_name(self):
        ingredient = Ingredient.objects.get(id = 1)

        field_label = ingredient._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')

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

    def test_ingredient_pic(self):
        ingredient = Ingredient.objects.get(id = 1)

        field_label = ingredient._meta.get_field('pic').verbose_name

        self.assertEqual(field_label, 'pic')

    def test_get_absolute_url(self):
        ingredient = Ingredient.objects.get(id = 1)

        self.assertEqual(ingredient.get_absolute_url(), '/ingredients/list/1')

class IngredientFormTest(TestCase):
    def test_ingredient_form_is_valid(self):
        form = CreateIngredientForm(
            data = {
                'name': 'Test name',
                'price': '13',
                'ingredient_unit_type': 'kilogram',
                'pic': tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
        )

        self.assertTrue(form.is_valid())

    def test_ingredient_form_name_is_not_valid(self):
        form = CreateIngredientForm(
            data = {
                'name': 'Test nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasdTest nameasdasdasdasdasdasdasd',
                'price': '13',
                'ingredient_unit_type': 'kilogram',
                'pic': tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
        )

        self.assertFalse(form.is_valid())

    def test_ingredient_form_price_is_not_valid(self):

        form = CreateIngredientForm(
            data = {
                'name': 'Test name',
                'price': 'asd',
                'ingredient_unit_type': 'kilogram',
                'pic': tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
        )

        self.assertFalse(form.is_valid())

    def test_ingredient_form_ingredient_unit_type_is_not_valid(self):

        form = CreateIngredientForm(
            data = {
                'name': 'Test name',
                'price': '13',
                'ingredient_unit_type': 'gram',
                'pic': tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
        )

        self.assertFalse(form.is_valid())
