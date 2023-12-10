#import
from django import forms

SEARCH_MODEL_CHOICES = (
    ('#1', 'Recipes'),
    ('#2', 'Ingredients')
)

CHART_CHOICES = (
    ('#1', 'Bar chart (Recipe)'),
    ('#2', 'Pie chart (Recipe)'),
    ('#3', 'Line chart (Ingredient)'),
    ('#4', 'None')
)

class SearchForm(forms.Form):
    search_criteria = forms.CharField(max_length = 200, required=False)
    model_choice = forms.ChoiceField(choices = SEARCH_MODEL_CHOICES)
    chart_type = forms.ChoiceField(choices= CHART_CHOICES)