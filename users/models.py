from django.db import models
from django.contrib.auth.models import User as UserAuth

# Create your models here.
class User(models.Model):
    user_info = models.OneToOneField(
        UserAuth,
        null = True,
        on_delete=models.CASCADE
    )
    favorite_recipes = models.ManyToManyField(
        'recipes.Recipe',
        related_name = "favorite_recipes",
        blank=True
    )
    created_recipes = models.ManyToManyField(
        'recipes.Recipe',
        related_name="created_recipes",
        blank=True
    )

    def __str__(self):
        return f"Username: {self.user_info.username}, ID: {self.id}"