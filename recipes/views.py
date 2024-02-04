from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView
import pandas as pd
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#imported models and fuctions from Project
from .forms import SearchForm, CreateRecipeForm
from .models import Recipe
from ingredients.models import Ingredient
from ingredients.forms import CreateIngredientForm
from users.models import User
from .utils import get_username_from_id, make_clickable_recipe, \
    make_clickable_ingredient, get_chart
from recipe_project.views import profile_absolute_url

# Create your views here.
def home(request):
    profile_url = profile_absolute_url(request)

    context = {
        "profile_url": profile_url
    }

    return render(request, "recipes/home.html", context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_url = profile_absolute_url(self.request)

        context["profile_url"] = profile_url

        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_url = profile_absolute_url(self.request)
        context["profile_url"] = profile_url
        
        user = self.request.user
        context["user"] = user

        return context
    
class UpdateRecipeView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form = CreateRecipeForm
    fields = ["name", "cooking_time", "recipe_directions", "pic"]
    template_name = 'recipes/update_recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_url = profile_absolute_url(self.request)
        context["profile_url"] = profile_url
        
        user = self.request.user
        context["user"] = user

        return context
    
class UpdateRecipeIngredients(LoginRequiredMixin, View):
    def get(self, request, pk):
        recipe = Recipe.objects.get(id = pk)
        user = User.objects.get(user_info__id = self.request.user.id)
        all_ingredients = Ingredient.objects.all()

        profile_url = profile_absolute_url(self.request)

        context = {
            "recipe": recipe,
            "all_ingredients": all_ingredients,
            'profile_url': profile_url
        }

        if user.id == recipe.creator.id:
            return render(request, 'recipes/update_recipe_ingredients.html', context)
        else:
            return redirect('/recipes/list/' + pk + '/')
        
    def post(self, request, pk):
        recipe = Recipe.objects.get(id = pk)

        try:
            add_ingredients = request.POST.get('add-ingredients').split(', ')
        except:
            add_ingredients = None

        try:
            create_ingredients = request.POST.get('create-ingredients').split(', ')
        except:
            create_ingredients = None

        try:
            remove_ingredients = request.POST.get('remove-input').split(', ')
        except:
            remove_ingredients = None

        if add_ingredients or create_ingredients:
            if len(add_ingredients[0]) > 0:
                for ingredient in add_ingredients:
                    try:
                        add_ingredient = Ingredient.objects.get(name = ingredient)

                        recipe.ingredients.add(add_ingredient)
                        add_ingredient.recipe_appearance.add(recipe)

                        recipe.save()
                        add_ingredient.save()
                    except:
                        print('Ingredient is not in the database.')

            if create_ingredients[0]:
                for index, ingredient in enumerate(create_ingredients):
                    name = request.POST.get('ingredient_name' + str(index))
                    price = request.POST.get('ingredient_price' + str(index))
                    ingredient_unit_type = request.POST.get(
                        'ingredient_unit_type' + str(index)
                    )
                    pic = request.FILES.get('ingredient_pic'+ str(index))

                    print(pic)

                    if not pic:
                        pic = 'no_picture.jpg'
                    

                    try:
                        add_ingredient = Ingredient.objects.create(
                            name = name,
                            price = price,
                            ingredient_unit_type = ingredient_unit_type,
                            pic = pic
                        )

                        recipe.ingredients.add(add_ingredient)
                        add_ingredient.recipe_appearance.add(recipe)

                        add_ingredient.save()

                    except:
                        print('Add new ingredient failed.')

        if remove_ingredients:

            for ingredient in remove_ingredients:
                remove_ingredient = Ingredient.objects.get( name = ingredient)

                recipe.ingredients.remove(remove_ingredient)
                remove_ingredient.recipe_appearance.remove(recipe)

                recipe.save()
                remove_ingredient.save()
                
                if remove_ingredient.recipe_appearance.count() == 0:
                    remove_ingredient.delete()

        return redirect('/recipes/list/' + pk + '/')

class DeleteRecipe(LoginRequiredMixin, View):
    def get(self, request, pk):
        recipe = Recipe.objects.get(id = pk)
        user = User.objects.get(user_info__id = self.request.user.id)

        profile_url = profile_absolute_url(self.request)

        context = {
            'recipe': recipe,
            'profile_url': profile_url
        }

        if user.id == recipe.creator.id:
            return render(request, 'recipes/delete_recipe.html', context)
        else:
            return redirect('/recipes/list/' + pk + '/')


    def post(self, request, pk):   
        recipe = Recipe.objects.get(id = pk)
        user = User.objects.get(id = recipe.creator.id)
        favorite_lists = User.objects.filter(favorite_recipes = recipe)

        user_confirmation = self.request.POST.get('delete-checkbox')

        if user_confirmation:
            for favorite in favorite_lists:
                favorite.favorite_recipes.remove(recipe)

            for ingredient in recipe.ingredients.all():
                ingredient.recipe_appearance.remove(recipe)
                ingredient.save()

                if ingredient.recipe_appearance.count() == 0:
                        ingredient.delete()

            user.created_recipes.remove(recipe)
            user.save()

            recipe.delete()

        return redirect('recipes:recipe_list')





@login_required
def search_view(request):
    form = SearchForm( request.POST or None )
    search_df = None
    chart = None

    if request.method == 'POST':
        search_criteria = request.POST.get('search_criteria')
        model_choice = request.POST.get('model_choice')
        chart_type = request.POST.get('chart_type')
        current_host = request.get_host()

        if request.is_secure():
            protocol = "https://" 
        else:
            protocol ="http://"

        if model_choice == '#1':
            qs = Recipe.objects.filter(name__contains= search_criteria)

            if qs:

                search_df = pd.DataFrame(qs.values())

                try:
                    search_df['creator'] = search_df['creator_id'].apply(get_username_from_id)
                except:
                    search_df['creator'] = 'Unknown'

                search_df['url'] = protocol + current_host + search_df['id'].apply(make_clickable_recipe)

                chart = get_chart(
                    chart_type, 
                    model_choice, 
                    search_df,
                    labels = search_df['difficulty']
                )
                
                search_df = search_df.to_html(render_links=True)

        if model_choice == '#2':
            qs = Ingredient.objects.filter(name__contains= search_criteria)

            if qs:

                search_df = pd.DataFrame(qs.values())

                search_df['url'] = protocol + current_host + search_df['id'].apply(make_clickable_ingredient)

                chart = get_chart(
                    chart_type, 
                    model_choice, 
                    search_df,
                    labels = search_df['name']
                )
                
                search_df = search_df.to_html(render_links=True)

    profile_url = profile_absolute_url(request)

    context = {
        'form': form,
        'search_df': search_df,
        'chart': chart,
        'profile_url': profile_url
    }
    
    return render( request, 'recipes/search.html', context )

@login_required
def create_recipe_view(request):

    all_ingredients = Ingredient.objects.all()
    ingr_form = CreateIngredientForm(request.POST or None)
    rec_form = CreateRecipeForm(request.POST or None)

    if request.method == "POST":
            user = User.objects.get(user_info__id = request.user.id)

            name = request.POST.get('name')
            cooking_time = request.POST.get('cooking_time')
            recipe_directions = request.POST.get('recipe_directions')
            creator = user
            pic = request.FILES.get('pic')

            if not pic:
                pic = 'no_picture.jpg'

            created_recipe = Recipe.objects.create(
                name = name,
                cooking_time = cooking_time,
                recipe_directions = recipe_directions,
                creator = creator,
                pic = pic
            )

            created_recipe.calculate_difficulty()

            created_recipe.save()

            user.created_recipes.add(created_recipe)

            user.save()

            ingredients = request.POST.get('ingredient_name_inputs').split(", ")

            for index, ingredient in enumerate(ingredients):
                try: 
                    add_ingredient = Ingredient.objects.get(name = ingredient)
                    created_recipe.ingredients.add(add_ingredient)
                    add_ingredient.recipe_appearance.add(created_recipe)
                    
                except:
                    ingredient_name = request.POST.get('ingredient_name' + str(index))
                    ingredient_price = request.POST.get('ingredient_price' + str(index))
                    ingredient_unit_type = request.POST.get(
                        'ingredient_unit_type' + str(index)
                    )

                    ingredient_picture = request.FILES.get('ngredient_pic' + str(index))

                    if not ingredient_picture:
                        ingredient_picture = 'no_picture.jpg'

                    add_ingredient = Ingredient.objects.create(
                        name = ingredient_name,
                        price = ingredient_price,
                        ingredient_unit_type = ingredient_unit_type,
                        pic = ingredient_picture
                    )

                    add_ingredient.recipe_appearance.add(created_recipe)
                    created_recipe.ingredients.add(add_ingredient)

            return redirect('/recipes/list/' + str(created_recipe.id))
    
    profile_url = profile_absolute_url(request)
        
    context = {
        "all_ingredients" : all_ingredients,
        "ingr_form": ingr_form,
        "rec_form": rec_form,
        'profile_url': profile_url
    }

    return render(request, 'recipes/create_recipe.html', context)