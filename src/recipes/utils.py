from django.shortcuts import reverse
from users.models import User
from .models import Recipe

def get_username_from_id(val):
    username = User.objects.get(id = val).username

    return username

def make_clickable(val):
    recipe = Recipe.objects.get(id = val)
    recipeURL = recipe.get_absolute_url()

    return recipeURL