#import
from django import forms
from ingredients.models import Ingredient

SEARCH_MODEL_CHOICES = (
    ('#1', 'Recipes'),
    ('#2', 'Ingredients')
)

CHART_CHOICES = (
    ('#1', 'Bar chart (Recipe)'),
    ('#2', 'Pie chart (Ingredient)'),
    ('#3', 'Line chart (Recipe)'),
    ('#4', 'None')
)

quantity_unit_choices = (
    ('milliliter', 'Milliliter'),
    ('gram', 'Gram')
)

class SearchForm(forms.Form):
    search_criteria = forms.CharField(max_length = 200, required=False)
    model_choice = forms.ChoiceField(choices = SEARCH_MODEL_CHOICES)
    chart_type = forms.ChoiceField(choices= CHART_CHOICES)

class CreateRecipeForm(forms.Form):
    name = forms.CharField(max_length=120)
    cooking_time = forms.IntegerField()
    ingredients = forms.ModelMultipleChoiceField(
        queryset = Ingredient.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    ingredient_quantities = forms.CharField(
        max_length = 2000, 
        widget= forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        help_text='Add quantities of the ingredients in the format: ' + 
        '100, 50')
    recipe_directions = forms.CharField(
        widget= forms.Textarea(attrs={'rows': 5, 'cols': 40}), 
        required=False
    )
    pic = forms.ImageField(required=False)
