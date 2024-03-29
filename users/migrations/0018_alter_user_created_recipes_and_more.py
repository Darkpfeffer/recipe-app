# Generated by Django 4.2.7 on 2024-01-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0020_alter_recipe_creator'),
        ('users', '0017_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_recipes',
            field=models.ManyToManyField(blank=True, related_name='created_recipes', to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorite_recipes',
            field=models.ManyToManyField(blank=True, related_name='favorite_recipes', to='recipes.recipe'),
        ),
    ]
