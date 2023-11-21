from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    username = models.OneToOneField(User, max_length=120, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=120)
    birthday = models.DateField()
    favorite_recipes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Username: {self.username}, ID: {self.id}"