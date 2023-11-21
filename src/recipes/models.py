from django.db import models

quantity_unit_choices = (
    ('milliliter', 'Milliliter'),
    ('gram', 'Gram')
)

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField()
    ingredients = models.TextField(max_length=2000)
    ingredient_quantities = models.TextField(max_length=2000, null=True)
    difficulty = models.CharField(max_length=12)
    creator_id = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.name}, Difficulty: {self.difficulty}, "+\
            f"Cooking time (in minutes): {self.cooking_time}"