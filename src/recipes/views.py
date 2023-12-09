from django.shortcuts import render
from django.views.generic import ListView, DetailView
import pandas as pd
#imported models and fuctions from Project
from .forms import SearchForm
from .models import Recipe
from ingredients.models import Ingredient
from .utils import get_username_from_id, make_clickable

# Create your views here.
def home(request):
    return render(request, "recipes/home.html")

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

def search_view(request):
    form = SearchForm( request.POST or None )
    search_df = None

    if request.method == 'POST':
        search_criteria = request.POST.get('search_criteria')
        model_choice = request.POST.get('model_choice')

        if model_choice == '#1':
            qs = Recipe.objects.filter(name__contains= search_criteria)

            search_df = pd.DataFrame(qs.values())

            search_df['creator_id_id'] = search_df['creator_id_id'].apply(get_username_from_id)

            search_df['name'] = search_df['name'].apply(make_clickable)
            
            search_df = search_df.to_html(render_links=True)

        if model_choice == '#2':
            qs = Ingredient.objects.filter(name__contains= search_criteria)

            search_df = pd.DataFrame(qs.values())
            
            search_df = search_df.to_html()

    context = {
        'form': form,
        'search_df': search_df
    }

    return render( request, 'recipes/search.html', context )