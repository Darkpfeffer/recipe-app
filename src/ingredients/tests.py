from django.test import TestCase
from .models import Ingredient

# Create your tests here.

class IngredientModelTest(TestCase):
    def setUpTestData():
        Ingredient.objects.create(
            name = "salt",
            supplier = "Someone",
            price = 0.50,
            price_unit = "Kilogram"
        )

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

    def test_ingredient_price_unit(self):
        ingredient = Ingredient.objects.get(id = 1)

        field_label = ingredient._meta.get_field('price_unit').verbose_name

        self.assertEqual(field_label, 'price unit')