#import
from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, \
search_view, create_recipe_view, recipe_success_view

#defining URLs and variables
app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipes/list/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/list/<pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/create/', create_recipe_view, name='create_recipe'),
    path('recipes/recipe_success', recipe_success_view, name='recipe_success'),
    path('search/', search_view, name='search')
]