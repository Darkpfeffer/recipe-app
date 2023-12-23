from django.views.generic import ListView, DetailView
from .models import Ingredient
from recipe_project.views import profile_absolute_url

# Create your views here.

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredients/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_url = profile_absolute_url(self.request)

        context["profile_url"] = profile_url

        return context


class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'ingredients/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_url = profile_absolute_url(self.request)

        context["profile_url"] = profile_url

        return context