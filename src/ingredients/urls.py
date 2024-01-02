#import
from django.urls import path
from .views import IngredientListView, IngredientDetailView, \
    create_ingredient_view, create_ingredient_success_view

#defining URLs and variables
app_name = 'ingredients'

urlpatterns = [
    path('list/', IngredientListView.as_view(), name='ingredient_list'),
    path('list/<pk>', IngredientDetailView.as_view(), name='ingredient_detail'),
    path('create/', create_ingredient_view, name='create_ingredient'),
    path('create/success', create_ingredient_success_view, name='create_ingredient_success')
]