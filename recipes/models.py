from django.db import models
from django.shortcuts import reverse

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
        help_text='Add quantities of the ingredients (value will be gram or milliliter ' +
        'based on the ingredient.) Write in quantities separated with comma and space (, ):' + 
        ' Example: 100, 50, 200')
    difficulty = models.CharField(max_length=12, blank=True, null=True, editable=False)
    recipe_cost = models.FloatField(blank=True, null=True, editable=False)
    creator = models.ForeignKey(
        'users.User', 
        on_delete=models.PROTECT,
        editable=False
    )
    recipe_directions = models.TextField(default="No directions added.")
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return f"{self.name}, Difficulty: {self.difficulty}, "+\
            f"Cooking time (in minutes): {self.cooking_time}"

    def get_absolute_url(self):
        return reverse('recipes:recipe_detail', kwargs={'pk': self.pk})
    
    def calculate_difficulty(self):
        short_cooking_time = int(self.cooking_time) < 10
        long_cooking_time = int(self.cooking_time) >= 10
        few_ingredients = self.ingredients.count() < 4    
        numerous_ingredients = self.ingredients.count() >= 4

        print("Difficulty calculation begins.. \n")

        if short_cooking_time and few_ingredients and self.difficulty != "Easy":
            self.difficulty = "Easy"
            self.save()
            print("Difficulty is changed to 'Easy' in the database.")
        elif short_cooking_time and numerous_ingredients and self.difficulty != "Medium":
            self.difficulty = "Medium"
            self.save()
            print("Difficulty is changed to 'Medium' in the database.")


        elif long_cooking_time and few_ingredients and self.difficulty != "Intermediate":
            self.difficulty = "Intermediate"
            self.save()
            print("Difficulty is changed to 'Intermediate' in the database.")

        elif long_cooking_time and numerous_ingredients and self.difficulty != "Hard":
            self.difficulty = "Hard"
            self.save()
            print("Difficulty is changed to 'Hard' in the database.")
        else:
            print("Difficulty is correct in the database. \n")
        
        print("Difficulty calculation ends.")