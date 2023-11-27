from django.db import models
import recipes.models

# Create your models here.
price_unit_choices = (
    ('liter', 'Liter'),
    ('kilogram', 'Kilogram')
)

class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    supplier = models.CharField(max_length=120, blank=True, null=True)
    price = models.FloatField(help_text='The value is in dollar')
    ingredient_unit_type = models.CharField(
        choices=price_unit_choices, 
        default='kilogram', 
        max_length=8)
    recipe_appearance = models.ManyToManyField(
        'recipes.Recipe', 
        blank=True
    )

    def __str__(self):
        return f"id = {self.id}, name = {self.name}"