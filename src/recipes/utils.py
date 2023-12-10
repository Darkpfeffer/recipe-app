from django.shortcuts import reverse
from io import BytesIO
import base64
import matplotlib.pyplot as plt
#Import function and models from Project
from users.models import User
from .models import Recipe
from ingredients.models import Ingredient

#Write your functions here:

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

def get_graph():
    buffer = BytesIO()

    #Save plot as file-like object
    plt.savefig(buffer, format='png')

    #set cursor back to the beginning
    buffer.seek(0)

    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png).decode('utf-8')

    buffer.close()

    return graph

def get_chart(chart_type, model_choice, data, **kwargs):
    plt.switch_backend('AGG')

    #specify figure size
    fig = plt.figure(figsize = (6,3))

    user_occurrence = Recipe.objects.filter(creator_id_id = data['creator_id_id']).count()
    ingredient_occurrence = Ingredient.objects.get(id = data['id']).recipe_appearance.count()

    if chart_type == '#1' and model_choice == '#1':
        plt.bar(data['creator_id_username'], data[user_occurrence])

    elif chart_type == '#2' and model_choice == '#2':
        labels=kwargs.get('labels')
        plt.pie(data[ingredient_occurrence], labels=labels)

    elif chart_type == '#3' and model_choice == '#1':
        plt.plot(data['name'], data['cooking_time'])

    elif chart_type == '#4':
        print('No chart type chosen.')

    else:
        print('Unknown chart type.')

    plt.tight_layout()

    chart = get_graph()
    return chart