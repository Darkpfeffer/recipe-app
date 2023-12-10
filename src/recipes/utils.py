from django.shortcuts import reverse
from users.models import User
from .models import Recipe
from ingredients.models import Ingredient

def get_username_from_id(val):
    username = User.objects.get(id = val).username

    return username

def make_clickable_recipe(val):
    recipe = Recipe.objects.get(id = val)
    recipeURL = recipe.get_absolute_url()

    return recipeURL

def make_clickable_ingredient(val):
    ingredient = Ingredient.objects.get(id = val)
    ingredientURL = ingredient.get_absolute_url()

    return ingredientURL