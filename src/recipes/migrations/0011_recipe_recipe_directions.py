# Generated by Django 4.2.7 on 2023-11-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_recipe_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_directions',
            field=models.TextField(default='No directions added.'),
        ),
    ]