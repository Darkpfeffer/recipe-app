from io import BytesIO
import base64
import matplotlib.pyplot as plt
#Import function and models from Project
from users.models import User
from .models import Recipe
from ingredients.models import Ingredient

#Write your functions here:

def get_username_from_id(val):
    username = User.objects.get(id = val).user_info.username

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

    if chart_type == '#1' and model_choice == '#1':
        recipes = Recipe.objects.all()

        all_difficulties = []
        difficulty_types = []
        difficulty_appearances = []


        for recipe in recipes:
            all_difficulties.append(recipe.difficulty)

        for difficulty in all_difficulties:
            if difficulty_types.__contains__(difficulty):
                continue
            else:
                difficulty_types.append(difficulty)

        for index, difficulty in enumerate(difficulty_types):
            difficulty_appearances.append(all_difficulties.count(difficulty_types[index]))
        
        plt.bar(difficulty_types, difficulty_appearances)

    elif chart_type == '#2' and model_choice == '#2':
        recipes = Recipe.objects.all()
        all_ingredient_list = []
        ingredients_count = []
        for recipe in recipes:
            for ingredient in recipe.ingredients.all():
                all_ingredient_list.append(ingredient.name)
        
        labels=kwargs.get('labels')
        for data_item in data['name'].values:
            ingredients_count.append(all_ingredient_list.count(data_item))

        plt.pie(ingredients_count, labels=labels)

    elif chart_type == '#3' and model_choice == '#1':
        plt.plot(data['name'], data['cooking_time'])

    elif chart_type == '#4':
        print('No chart type chosen.')

    else:
        print('Unknown chart type.')

    plt.tight_layout()

    chart = get_graph()
    return chart