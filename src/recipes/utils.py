from users.models import User
from .models import Recipe

def get_username_from_id(val):
    username = User.objects.get(id = val).username

    return username

def make_clickable(val):
    recipe = Recipe.objects.get(name = val)
    recipeURL = recipe.get_absolute_url()

    return f'<a href="{recipeURL}>{recipe.name}<a>'