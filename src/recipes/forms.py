#import
from django import forms

SEARCH_MODEL_CHOICES = (
    ('#1', 'Recipes'),
    ('#2', 'Ingredients')
)

class SearchForm(forms.Form):
    search_criteria = forms.CharField(max_length = 200)
    model_choice = forms.ChoiceField(choices = SEARCH_MODEL_CHOICES)