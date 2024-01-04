#import
from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, search_view, check_ingredient_view

#defining URLs and variables
app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipes/list/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/list/<pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/ingredient-check/', check_ingredient_view, name='check_ingredient'),
    path('search/', search_view, name='search')
]