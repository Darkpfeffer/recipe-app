from django.db import models
from django.shortcuts import reverse
import recipes.models

# Create your models here.
price_unit_choices = (
    ('liter', 'Liter'),
    ('kilogram', 'Kilogram')
)

class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField(help_text='The value is in dollar. '+\
                              'Add the average price of the ingredient. ' +\
                                'Measures are in "kilogram" and "liter".')
    ingredient_unit_type = models.CharField(
        choices=price_unit_choices, 
        default='kilogram', 
        max_length=8)
    recipe_appearance = models.ManyToManyField(
        'recipes.Recipe', 
        blank=True
    )
    pic = models.ImageField(upload_to='ingredients', default='no_picture.jpg')

    def __str__(self):
        return f"id = {self.id}, name = {self.name}"
    
    def get_absolute_url(self):
        return reverse('ingredients:ingredient_detail', kwargs={'pk': self.pk})