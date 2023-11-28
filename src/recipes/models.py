from django.db import models
import users.models
import ingredients.models

quantity_unit_choices = (
    ('milliliter', 'Milliliter'),
    ('gram', 'Gram')
)

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField()
    ingredients = models.ManyToManyField(
        'ingredients.Ingredient',
        help_text='Enter ingredients at the Ingredient table first.'
    )
    ingredient_quantities = models.TextField(
        max_length=2000, 
        null=True,
        help_text='Add quantities of the ingredients in the format: ' + 
        '(100, gram), (50, milliliter)')
    difficulty = models.CharField(max_length=12, blank=True, null=True)
    recipe_cost = models.FloatField(blank=True, null=True)
    creator_id = models.ForeignKey('users.User', on_delete=models.PROTECT)
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return f"{self.name}, Difficulty: {self.difficulty}, "+\
            f"Cooking time (in minutes): {self.cooking_time}"