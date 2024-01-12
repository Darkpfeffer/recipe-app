from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
import pandas as pd
from django.contrib.auth.decorators import login_required
#imported models and fuctions from Project
from .forms import SearchForm, CreateRecipeForm
from .models import Recipe
from ingredients.models import Ingredient
from ingredients.forms import CreateIngredientForm, CreateIngredientAtRecipeForm
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

        return context

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

                search_df['creator_id_id'] = search_df['creator_id_id'].apply(get_username_from_id)

                search_df['url'] = protocol + current_host + search_df['id'].apply(make_clickable_recipe)

                chart = get_chart(
                    chart_type, 
                    model_choice, 
                    search_df,
                    labels = search_df['name']
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
    ingr_to_database = CreateIngredientAtRecipeForm(request.POST or None)

    if request.method == "POST":
        new_ingredients = request.POST.get('inputs').split("//, ")
        
        for ingredient in new_ingredients:
            ingredient_attributes = ingredient.split(", ")

            Ingredient.objects.create(
                name = ingredient_attributes[0],
                price = ingredient_attributes[1],
                ingredient_unit_type = ingredient_attributes[2]
            )


        return redirect('recipes:create_recipe')

    context = {
        "all_ingredients" : all_ingredients,
        "ingr_form": ingr_form,
        "ingr_to_database": ingr_to_database,
        "rec_form": rec_form
    }

    return render(request, 'recipes/create_recipe.html', context)