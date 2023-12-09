from django.views.generic import ListView, DetailView
from .models import Ingredient

# Create your views here.

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredients/main.html'

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'ingredients/detail.html'