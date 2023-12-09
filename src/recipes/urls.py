#import
from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, search_view

#defining URLs and variables
app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipes/list/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/list/<pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('search/', search_view, name='search')
]