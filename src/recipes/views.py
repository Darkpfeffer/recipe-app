from django.shortcuts import render
from django.views.generic import ListView, DetailView
import pandas as pd
from django.contrib.auth.decorators import login_required
#imported models and fuctions from Project
from .forms import SearchForm
from .models import Recipe
from ingredients.models import Ingredient
from .utils import get_username_from_id, make_clickable_recipe, make_clickable_ingredient

# Create your views here.
def home(request):
    return render(request, "recipes/home.html")

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

@login_required
def search_view(request):
    form = SearchForm( request.POST or None )
    search_df = None

    if request.method == 'POST':
        search_criteria = request.POST.get('search_criteria')
        model_choice = request.POST.get('model_choice')
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
                
                search_df = search_df.to_html(render_links=True)

        if model_choice == '#2':
            qs = Ingredient.objects.filter(name__contains= search_criteria)

            if qs:

                search_df = pd.DataFrame(qs.values())

                search_df['url'] = protocol + current_host + search_df['id'].apply(make_clickable_ingredient)
                
                search_df = search_df.to_html(render_links=True)

    context = {
        'form': form,
        'search_df': search_df
    }

    
    return render( request, 'recipes/search.html', context )