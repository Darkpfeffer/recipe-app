from django import forms

class CreateIngredientForm(forms.Form):
    price_unit_choices = (
    ('liter', 'Liter'),
    ('kilogram', 'Kilogram')
    )
    name = forms.CharField(max_length=120)
    price = forms.FloatField(help_text='The value is in dollar. '+\
                              'Add the average price of the ingredient. ' +\
                                'Measures are in "kilogram" and "liter".')
    ingredient_unit_type = forms.ChoiceField(
        choices=price_unit_choices)
    pic = forms.ImageField(required=False)