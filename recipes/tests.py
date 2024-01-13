from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from .models import Recipe
from users.models import User
from ingredients.models import Ingredient
from .forms import SearchForm
from .views import search_view

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Ingredient.objects.create(
            name = "salt",
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
            recipe_cost = 25.03,
            creator_id = test_user,
            recipe_directions = "lorem ipsum",
            pic='no_picture.jpg'
        )

        test_recipe = Recipe.objects.get(id=1)

        test_recipe.ingredients.set(test_ingredient_query)

        test_ingredient.recipe_appearance.add(test_recipe)

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

    def test_recipe_ingredient_quantities(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('ingredient_quantities').verbose_name

        self.assertEqual(field_label, 'ingredient quantities')

    def test_recipe_difficulty(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('difficulty').verbose_name

        self.assertEqual(field_label, 'difficulty')

    def test_recipe_recipe_cost(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('recipe_cost').verbose_name

        self.assertEqual(field_label, 'recipe cost')

    def test_recipe_creator_id(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('creator_id').verbose_name

        self.assertEqual(field_label, 'creator id')

    def test_recipe_recipe_directions(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('recipe_directions').verbose_name

        self.assertEqual(field_label, 'recipe directions')

    def test_recipe_pic(self):
        recipe = Recipe.objects.get(id = 1)

        field_label = recipe._meta.get_field('pic').verbose_name

        self.assertEqual(field_label, 'pic')

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id = 1)

        self.assertEqual(recipe.get_absolute_url(), '/recipes/list/1')

    def test_calculate_difficulty(self):
        recipe = Recipe.objects.get(id = 1)

        self.assertEqual(recipe.difficulty, 'Intermediate')

        
class SearchFormTest(TestCase):
    def test_search_form_search_is_valid(self):
        form = SearchForm(data= {
            'search_criteria': 'hot',
            'model_choice': '#1',
            'chart_type': '#1'
        })

        self.assertTrue(form.is_valid())

    def test_search_form_blank_search_criteria(self):
        form = SearchForm(data = {
            'search_criteria': '',
            'model_choice': '#1',
            'chart_type': '#1'
        })

        self.assertTrue(form.is_valid())

    def some(self):
        form = SearchForm(data = {
            'search_criteria': 'asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd',
            'model_choice': '#1',
            'chart_type': '#1'
        })

        self.assertFalse(form.is_valid())

class SearchViewTest(TestCase):
    def setUpTestData():
        user= get_user_model().objects.create_user(
            username = 'testuser', password='secret'
        )

        User.objects.create(
            username = user,
            name = "Erik Vasquez",
            email = "vasquez@example.com",
            birthday = "1212-12-12"
        )

    def test_search_view_requires_login(self):
        user = User.objects.get(id = 1)
        
        factory = RequestFactory()

        request = factory.get(reverse('recipes:search'))

        request.user = user.username

        response = search_view(request)

        self.assertEqual(response.status_code, 200)