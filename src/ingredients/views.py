from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ingredient

# Create your views here.

class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'ingredients/main.html'

class IngredientDetailView(LoginRequiredMixin, DetailView):
    model = Ingredient
    template_name = 'ingredients/detail.html'