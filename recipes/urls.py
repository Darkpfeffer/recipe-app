#import
from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, \
UpdateRecipeView, search_view, create_recipe_view, \
UpdateRecipeIngredients, DeleteRecipe

#defining URLs and variables
app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipes/list/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/list/<pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/list/<pk>/update_recipe/', UpdateRecipeView.as_view(), name='recipe_update'),
    path(
            'recipes/list/<pk>/update_recipe_ingredients/', 
            UpdateRecipeIngredients.as_view(), name='update_recipe_ingredients' 
        ),

    path('recipes/create/', create_recipe_view, name='create_recipe'),
    path('recipes/list/<pk>/delete_recipe/', DeleteRecipe.as_view(), 
         name='delete_recipe'
         ),

    path('search/', search_view, name='search')
]