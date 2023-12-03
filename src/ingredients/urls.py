#import
from django.urls import path
from .views import IngredientListView, IngredientDetailView

#defining URLs and variables
app_name = 'ingredients'

urlpatterns = [
    path('ingredients/list/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/list/<pk>', IngredientDetailView.as_view(), name='ingredient_detail')
]