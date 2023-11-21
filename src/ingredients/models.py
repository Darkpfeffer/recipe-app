from django.db import models

# Create your models here.
price_unit_choices = (
    ('liter', 'Liter'),
    ('kilogram', 'Kilogram')
)

class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    supplier = models.CharField(max_length=120, blank=True, null=True)
    price = models.FloatField()
    price_unit = models.CharField(choices=price_unit_choices, default='kilogram', max_length=8)

    def __str__(self):
        return f"id = {self.id}, name = {self.name}"